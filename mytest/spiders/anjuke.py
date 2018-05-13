# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'

    def start_requests(self):
        yield scrapy.Request(url='https://beijing.anjuke.com/sale/',headers={'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
})
    def parse(self, response):
        test=response.xpath(r'//*[@id="houselist-mod-new"]/li[1]/div[2]/div[1]/a/text()').extract()
        print(test)
