# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    news_id = scrapy.Field()
    url = scrapy.Field()


    # pass
