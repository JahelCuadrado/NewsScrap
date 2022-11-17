import os
import sys

sys.path.append('E:\\Escritorio\\Trabajo\\Proyectos Django\\NewsScrap\\newsscrap')

import django
from twisted.internet.task import LoopingCall
from twisted.internet      import reactor
from scrapy.selector       import Selector
from django.apps           import AppConfig
from scrapy.spiders        import Rule
from scrapy.crawler        import CrawlerRunner
from scrapy.selector       import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders        import CrawlSpider

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'newsscrap.settings.local')
django.setup()
from applications.publico.models   import NoticiasPublico



class ExtractorPublico(CrawlSpider, AppConfig):

    name = "Noticias"

    custom_settings = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.publico.es/politica#analytics-cabecera-comprimida:submenu']

    download_delay = 2

    rules = (
        Rule(
            LinkExtractor(
                allow=r'l#analytics-seccion:listado'
            ),follow=True, callback="parse_noticias"
        ),
    )

    def parse_noticias(self, response):
        
        response = Selector(response)

        enlace = response.xpath("//body/@data-url")

        titulo = response.xpath("//h1/text()")

        imagen = response.xpath("//img[@class='ImagenAperturaClick']/@src")

        descripcion = response.xpath("//div[@class='article-header-epigraph col-12']/h2/text()")
        
        datos = NoticiasPublico(
            titulo = titulo.get(),
            descripcion = descripcion.get(),
            url = "https://www.publico.es"+enlace.get(),
            imagen = "https://www.publico.es"+imagen.get()
        )
        
        datos.save()
        
        print('Noticias extraidas')


runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorPublico))
task.start(7200)
reactor.run()