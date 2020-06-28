# -*- coding: utf-8 -*-
import scrapy


class BaiduSpiderSpider(scrapy.Spider):
    # name是spider的名称--将来启动spider爬虫的需要使用
    name = 'baidu_spider'
    # allowed_domains 二次请求需要下载的域名
    # allowed_domains = ['www.baidu.com']
    # 需要让scrapy开始爬取的url，相当于base_url
    # 只需要将base_url 放入倒start_urls中，scrapy启动之后，救会从里面取url进行下载
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        '''
        处理下载器传送过来的response，处理response提取数据，或发送二次请求
        :param response:获取相应的内容，response.text--str类型 response.body--bytes类型
        :return:
        '''
        with open('baidu.html','w',encoding='UTF-8') as fp:
            fp.write(response.text)
        print(1)
