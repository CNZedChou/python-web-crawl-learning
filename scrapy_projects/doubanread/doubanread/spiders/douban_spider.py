# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # allowed_domains = ['www']
    start_urls = ['https://read.douban.com/charts']
    # 由于有部分request使用selenium，有部分使用request
    # 所以需要通过一个参数可以标识请求（request）
    # 对于初始请求，如果想要像二次请求那样自定义request对象
    """
    scrapy.Request(
        meta={},
    )
    """
    def parse(self, response):
        pass
