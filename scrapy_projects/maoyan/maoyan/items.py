# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    movie_title = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_date = scrapy.Field()
    movie_score = scrapy.Field()
    movie_detail = scrapy.Field()

