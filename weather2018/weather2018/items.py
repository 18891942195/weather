# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Weather2018Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    day=scrapy.Field()
    wea=scrapy.Field()
    tem=scrapy.Field()
    win1=scrapy.Field()
    win2=scrapy.Field()
    power=scrapy.Field()
