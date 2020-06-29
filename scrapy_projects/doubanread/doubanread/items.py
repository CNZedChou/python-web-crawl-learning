# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanreadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    book_url = scrapy.Field()
    author = scrapy.Field()
    wordCount = scrapy.Field()
    desc = scrapy.Field()
    read_num = scrapy.Field()
    collect_num = scrapy.Field()
    monthly_ticket = scrapy.Field()
    total_ticket = scrapy.Field()
    book_id = scrapy.Field()
