# -*- coding: utf-8 -*-
import time

import scrapy

from biquge.items import BiqugeItem


class BiqugeSpiderSpider(scrapy.Spider):
    name = 'biquge_spider'
    # allowed_domains = ['www']
    start_urls = ['http://www.xbiquge.la/xuanhuanxiaoshuo/']

    def parse(self, response):
        # print(response.text.replace(u'\xa0', u''))
        book_url = response.xpath('//*[@id="newscontent"]/div[1]/ul/li[1]/span[1]/a/@href').extract()
        for url in book_url:
            # 发送二次请求
            yield scrapy.Request(url,callback=self.parse_book,encoding="utf-8")


    def parse_book(self,response):
        # 在每本书的页面中获取章节url
        chapter_urls = response.xpath('//div[@id="list"]/dl/dd/a/@href').extract()
        # print(chapter_urls)
        for url in chapter_urls:
            # 由于在章节中的url不是完整的url是相对url，所以将书的url拼接起来
            full_url = response.urljoin(url)
            time.sleep(2)
            yield scrapy.Request(full_url,callback=self.parse_chapter,encoding="utf-8")

    def parse_chapter(self,response):
        # 提取数据
        item = BiqugeItem()
        book_name = response.xpath('//div[@class="con_top"]/a[3]/text()').extract_first()
        chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()

        chapter_content = response.xpath('string(//div[@id="content"])').extract()
        # 在xpath中有string() 语法可以使得提取到的文字保留格式
        chapter_url = response.url
        item['book_name']=book_name
        item['chapter_name']=chapter_name
        item['chapter_content']=chapter_content
        item['chapter_url']=chapter_url
        # print(item)
        yield item