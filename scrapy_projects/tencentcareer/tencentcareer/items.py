# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcareerItem(scrapy.Item):
    # define the fields for your item here like:
    career_name = scrapy.Field()
    career_city = scrapy.Field()
    career_date = scrapy.Field()
    career_detail = scrapy.Field()

