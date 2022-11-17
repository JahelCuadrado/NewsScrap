import os
import sys

sys.path.append('E:\\Escritorio\\Trabajo\\Proyectos Django\\NewsScrap\\newsscrap')

import django
from twisted.internet.task import LoopingCall
from twisted.internet      import reactor
from scrapy.spiders        import Spider
from scrapy.crawler        import CrawlerRunner
from scrapy.selector       import Selector
from django.apps           import AppConfig

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'newsscrap.settings.local')
django.setup()
from applications.xataka.models import NoticiasXataka


class ExtractorXataka(Spider, AppConfig):

    name = "Noticias"

    custom_settings = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.xataka.com/categoria/seleccion']
    
    def parse(self, response):
        
        response = Selector(response)
        
        enlaces = response.xpath("//article[contains(@class, 'recent-abstract abstract-article')]/div/div/a/@href")

        titulos = response.xpath("//article[contains(@class, 'recent-abstract abstract-article')]/div/header/h2/a/text()")

        imagenes = response.xpath("//article[contains(@class, 'recent-abstract abstract-article')]/div/div/a/picture/img/@src")

        descripciones = response.xpath("//article[contains(@class, 'recent-abstract abstract-article')]/div/div[contains(@class, 'abstract-excerpt')]/p/text()")

        for noticia in zip(enlaces, titulos, imagenes, descripciones):
            datos = NoticiasXataka(
                 titulo=noticia[1].get(),
                 descripcion=noticia[3].get(),
                 url=noticia[0].get(),
                 imagen=noticia[2].get())
            datos.save()
            print('Noticias extraidas')

runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorXataka))
task.start(7200)
reactor.run()