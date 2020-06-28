# -*- coding: utf-8 -*-
import scrapy

from hupu.items import HupuItem


class HupuSpiderSpider(scrapy.Spider):
    name = 'hupu_spider'
    # allowed_domains = ['www']
    start_urls = []
    for i in range(20,30):
        base_url = 'https://voice.hupu.com/nba/%s'
        start_urls.append(base_url % i)

    def parse(self, response):
        new_urls = response.xpath('//div[@class="news-list"]/ul/li//h4/a/@href').extract()
        # print(new_urls)
        for url in new_urls:
            yield scrapy.Request(url,callback = self.parse_detail,encoding='utf-8')


    def parse_detail(self,response):
        # 标题
        title = response.xpath('//h1[@class="headline"]/text()').extract_first()
        # print(title)
        source = response.xpath('//span[@id="source_baidu"]/a/text()').extract_first()
        images = response.xpath('//div[@class="artical-content"]//img/@src').extract()
        # print(images)
        content = response.xpath('string(//div[@class="artical-content"])').extract_first().strip()
        # print(content)
        date = response.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
        item = HupuItem()

        item['title'] = title
        item['source'] = source
        item['images'] = images
        item['content'] = content
        item['date'] = date
        item['url'] = response.url
        # print(item)
        # write_to_mongo(item)
        yield item