# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_content = scrapy.Field()
    chapter_url = scrapy.Field()
    hash_url = scrapy.Field()

