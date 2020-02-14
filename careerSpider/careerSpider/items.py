# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CareerspiderItem(scrapy.Item):
    name = scrapy.Field()
    industry = scrapy.Field()
    job = scrapy.Field()
    opt_cpt = scrapy.Field()
    sponsorship = scrapy.Field()
