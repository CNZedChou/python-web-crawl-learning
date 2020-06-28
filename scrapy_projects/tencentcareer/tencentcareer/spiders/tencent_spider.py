# -*- coding: utf-8 -*-
import scrapy

from tencentcareer.items import TencentcareerItem


class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'
    # allowed_domains = ['www']
    start_urls = []
    # 添加分页
    for i in range(1):
        base_url = 'https://careers.tencent.com/search.html?index=%s'% i
        start_urls.append(base_url)


    def parse(self, response):
        # 测试能否下载也买你
        # print(response.text.replace(u'\xa9',u''))
        # print('in spider ')
        # 提取数据
        item = TencentcareerItem()
        career = response.xpath('//div[@class="recruit-list"][-1]')
        career_name = career.xpath('//a/h4/text()').extract_first()
        print(career_name)
        # for i in range(1,11):
        #     item = TencentcareerItem()
        #     career = response.xpath('//div[@class="recruit-wrap recruit-margin"]/div[{}]'.format(i))
            # career_name = career.xpath('//a/h4/text()').extract_first()
            # career_city = career.xpath('//a/p[1]/span[2]/text()').extract_first()
            # career_date = career.xpath('//a/p[1]/span/text()').extract()
            # career_detail = career.xpath('//a/p[2]/text()').extract_first()
            # item['career_name'] = career_name
            # item['career_city'] = career_city
            # item['career_date'] = career_date
            # item['career_detail'] = career_detail
            # print(career)


