# -*- coding: utf-8 -*-
import scrapy
import re
import json

from doubanread.items import DoubanreadItem


class DoubanSpiderSpider(scrapy.Spider):
    # 当scrapy启动的时候，默认加载的方法只有一个：start_request()
    # 在start_request方法中，实质就是遍历start_url，取出url，发送请求
    # 当我们重写start_request()这个方法，那么当前spider，start_url就只是一个列表
    name = 'douban_spider'
    # allowed_domains = ['www']
    start_urls = []
    # 由于有部分request使用selenium，有部分使用request
    # 所以需要通过一个参数可以标识请求（request）
    # 对于初始请求，如果想要像二次请求那样自定义request对象
    """
    scrapy.Request(
        meta={},
    )
    """

    def start_requests(self):
        base_url = 'https://read.douban.com/charts'
        yield scrapy.Request(base_url, callback=self.parse, encoding='utf-8', meta={'flag': False})

    def parse(self, response):
        type_urls = response.xpath('//div[@class="rankings-nav"]/a[position()>1]/@href').extract()
        # print(type_urls)
        for url in type_urls:
            # /charts?type=unfinished_column&index=featured&dcs=charts&dcm=charts-nav
            p = re.compile(r'type=(.*?)&index=(.*?)&dcs')
            read_type = p.search(url).group(1)
            read_index = p.search(url).group(2)
            ajax_url = 'https://read.douban.com/j/index//charts?type={}&index={}&verbose=1'.format(read_type,read_index)
            yield scrapy.Request(ajax_url, callback=self.parse_ajax, encoding='utf-8', meta={'flag': True})

    def parse_ajax(self, response):
        json_str = response.text
        json_data = json.loads(json_str)
        if json_data is not None:
            for data in json_data['list']:
                title = data['works']['title']
                book_url = 'https://read.douban.com' + data['works']['url']
                author = data['works']['author'][0]['name']
                abstract = data['works']['abstract']
                wordCount = data['works']['wordCount']
                item = DoubanreadItem()
                item['title'] = title
                item['book_url'] = book_url
                item['author'] = author
                item['wordCount'] = wordCount
                # item只处理了一半，剩下一半在另外一个方法中。
                yield scrapy.Request(book_url, callback=self.parse_detail, encoding='utf-8',meta={'flag': True, 'data': item})

    def handle_number(self, text):
        '''
        处理带逗号的字符串数字
        :param num:2,111
        :return:
        '''
        if text is not None:
            p = re.compile(r'\d+')
            result = p.findall(text)
            return ''.join(result)

    def parse_detail(self, response):
        url = response.url
        item = response.meta['data']
        # 由于使用try catch 容易引起bug，所以在这里使用if 选择结构，在url中出现ebook，是except中的情况，可以直接分离出来
        if 'ebook' in url:
            desc = response.xpath('string(//div[@class="info"])').extract_first()
            # 阅读数
            read_num = response.xpath('//span[@class="read-count"]/text()').extract_first()
            # 收藏数
            collect_num = ''
            # 月票数
            monthly_ticket = ''
            # 累计推荐数
            total_ticket = ''
            # print(desc,read_num)
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = collect_num
            item['monthly_ticket'] = monthly_ticket
            item['total_ticket'] = total_ticket
        else:
            desc = response.xpath(
                'string(//div[@class="when-expand"]/p/text()|//div[@class="when-fold"]/text())').extract_first()
            # 阅读数
            read_num = response.xpath('//div[@class="count-group"]/span[2]/div[2]/text()').extract_first()
            # 收藏数
            collect_num = response.xpath('//div[@class="count-group"]/span[3]/div[2]/text()').extract_first()
            # 月票数
            monthly_ticket = response.xpath('//div[@class="count-group"]/span[4]/div[2]/text()').extract_first()
            # 累计推荐数
            total_ticket = response.xpath('//div[@class="count-group"]/span[5]/div[2]/text()').extract_first()
            # print(word_num,read_num,collect_num,monthly_ticket,total_ticket)
            # print(desc)
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = self.handle_number(collect_num)
            item['monthly_ticket'] = self.handle_number(monthly_ticket)
            item['total_ticket'] = self.handle_number(total_ticket)
        yield item
