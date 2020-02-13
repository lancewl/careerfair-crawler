import scrapy
from scrapy_splash import SplashRequest


class CareerFairSpider(scrapy.Spider):
    name = "careerfair_spider"
    start_urls = ['https://app.thefairsapp.com/#/fair/648/employers']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 0.5, 'http_method': 'GET'})


    def parse(self, response):
        EMPLOYER_SELECTOR = '.employer-collection-item'
        for employer in response.css(EMPLOYER_SELECTOR):
            NAME_SELECTOR = 'span ::text'
            URL_SELECTOR = 'a ::attr(href)'
            detail_page = employer.css(URL_SELECTOR).get()
            if detail_page:
                yield SplashRequest(url='https://app.thefairsapp.com/'+detail_page, callback=self.parse2, endpoint='render.html', args={'wait': 1, 'http_method': 'GET'})
    
    def parse2(self, response):
        CONTAINER_SELECTOR = '.employer-container'
        container = response.css(CONTAINER_SELECTOR)
        if container:
            NAME_SELECTOR = 'h5 ::text'
            yield {
                'name': container.css(NAME_SELECTOR).get(),
            }
        