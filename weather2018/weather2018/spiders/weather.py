# -*- coding: utf-8 -*-
import scrapy
from weather2018.items import Weather2018Item

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101110101.shtml']

    def parse(self, response):
        res=response.css("ul.t li")
        for li in res:
            items=Weather2018Item()
            items['day']=li.css("h1::text").extract_first()
            items['wea']=li.css("p.wea::attr(title)").extract_first()
            items['tem']=li.xpath("p[@class='tem']").xpath("string(.)").extract_first()
            items['win1']=li.xpath("p[@class='win']/em/span[1]/@title").extract_first()
            items['win2']=li.css("p.win").xpath("em/span[2]/@title").extract_first()
            items['power']=li.xpath("p[@class='win']/i/text()").extract_first()
            yield items

