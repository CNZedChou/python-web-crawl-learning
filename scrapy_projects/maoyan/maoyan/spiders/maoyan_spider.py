# -*- coding: utf-8 -*-
import scrapy

from maoyan.items import MaoyanItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    # allowed_domains = ['www']
    start_urls = []
    # 分页操作
    for i in range(10):
        base_url = 'https://maoyan.com/board/4?offset=%s'%(i * 10)
        start_urls.append(base_url)
        # print(1)

    def parse(self, response):
        # 测试下载器下载好的response有没有数据
        # print(response.text)
        # 提取数据

        item = MaoyanItem()
        '''
        response对象的xpath方法
        从selector中提取数据的方法
            response.xpath().extract_first() -- 就是一个字符串
            response.xpath().extract() -- 返回值是list，list里面是所有字符串的内容
        '''

        dd_list = response.xpath('//div[@class="main"]/dl/dd')
        # print(2)
        for dd in dd_list:
            movie_title = dd.xpath('.//p[@class="name"]/a/@title').extract_first()
            movie_actor = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            movie_date = dd.xpath('.//p[@class="releasetime"]/text()').extract_first()
            movie_score = dd.xpath('.//p[@class="score"]/i/text()').extract()
            movie_detail = dd.xpath('.//p[@class="name"]/a/@href').extract_first()
            # print(3)
            # 在网页中评分的个位数和小数是分开的，所以需要连接起来
            movie_score = "".join(movie_score)
            item['movie_title'] = movie_title
            item['movie_actor'] = movie_actor
            item['movie_date'] = movie_date
            item['movie_score'] = movie_score
            item['movie_detail'] = movie_detail
            # print(item)
            yield item



