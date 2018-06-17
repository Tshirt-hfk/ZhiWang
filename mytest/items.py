# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytestItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    orign = scrapy.Field()