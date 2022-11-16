import os
import sys

sys.path.append('E:\\Escritorio\\Trabajo\\Proyectos Django\\NewsScrap\\newsscrap')

import django
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from scrapy.spiders import Spider
from scrapy.crawler import CrawlerRunner
from scrapy.selector import Selector
from django.apps import AppConfig

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'newsscrap.settings.local')
django.setup()
from applications.anait.models import NoticiasAnait



class ExtractorAnait(Spider, AppConfig):

    name = "Noticias"

    custom_settings = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.anaitgames.com/noticias']
    
    def parse(self, response):
        
        response = Selector(response)
        
        enlaces = response.xpath("//article[starts-with(@id, 'post-') and contains(@class, 'post')]/a/@href")
        
        titulos = response.xpath("//article[starts-with(@id, 'post-') and contains(@class, 'post')]/div/header/h2/a/text()")
        
        imagenes = response.xpath("//article[starts-with(@id, 'post-') and contains(@class, 'post')]/a/img/@src")
        
        descripciones = response.xpath("//article[starts-with(@id, 'post-') and contains(@class, 'post')]/div/div/p/text()")

        for noticia in zip(enlaces, titulos, imagenes, descripciones):
            datos = NoticiasAnait(
                 titulo=noticia[1].get(),
                 descripcion=noticia[3].get(),
                 url=noticia[0].get(),
                 imagen=noticia[2].get())
            datos.save()
            print('Noticias extraidas')

runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorAnait))
task.start(60)
reactor.run()