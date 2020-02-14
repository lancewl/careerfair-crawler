import scrapy
from scrapy_splash import SplashRequest
from ..items import CareerspiderItem


class CareerFairSpider(scrapy.Spider):
    name = "careerfair_spider"
    start_urls = ['https://app.thefairsapp.com/#/fair/648/employers']

    custom_settings = {
        'FEED_EXPORT_FIELDS' : ["name", "industry", "job", "opt_cpt","sponsorship"]
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 3, 'http_method': 'GET'})


    def parse(self, response):
        EMPLOYER_SELECTOR = '.employer-collection-item'
        for employer in response.css(EMPLOYER_SELECTOR):
            NAME_SELECTOR = 'span ::text'
            URL_SELECTOR = 'a ::attr(href)'
            detail_page = employer.css(URL_SELECTOR).get()
            if detail_page:
                yield SplashRequest(url='https://app.thefairsapp.com/'+detail_page, callback=self.parse2, endpoint='render.html', args={'wait': 3, 'http_method': 'GET'})
    
    def parse2(self, response):
        items = CareerspiderItem()
        CONTAINER_SELECTOR = '.employer-container'
        container = response.css(CONTAINER_SELECTOR)
        if container:
            NAME_SELECTOR = '.solo-employer-header h5 ::text'
            IND_SELECTOR = ".whitelabel-text-primary:contains('Industry') + ul li ::text"
            JOB_SELECTOR = ".whitelabel-text-primary:contains('Job') + ul li ::text"
            OPTCPT_SELECTOR = ".whitelabel-text-primary:contains('OPT/CPT') + ul li ::text"
            VISA_SELECTOR = ".whitelabel-text-primary:contains('Sponsorship') + ul li ::text"
            items['name'] = container.css(NAME_SELECTOR).get()
            items['industry'] = container.css(IND_SELECTOR).extract() #extract multiple li element
            items['job'] = container.css(JOB_SELECTOR).extract() #extract multiple li element
            items['opt_cpt'] = container.css(OPTCPT_SELECTOR).get()
            items['sponsorship'] = container.css(VISA_SELECTOR).get()
            return items
        