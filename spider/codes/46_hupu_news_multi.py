# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  46_hupu_news.py
@Description    :  
@CreateTime     :  2020-6-28 11:35
------------------------------------
@ModifyTime     :  
"""
import hashlib
import threading
from queue import Queue
import requests
from lxml import etree
import pymongo


class HupuSipder(threading.Thread):
    def __init__(self,url,q_page):
        super().__init__()
        self.client = pymongo.MongoClient()
        self.db = self.client['hupu']
        self.url = url
        self.q_page = q_page



    def get_xpath(self,url):
        ''''
        请求url，获取页面内容的element对象
        '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4178.0 Safari/537.36 Edg/85.0.558.0',
        }
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return etree.HTML(response.text)
        else:
            return None


    def parse_page(self,url):
        '''
        解析每一个分页，获取列表页url
        :param url:
        :return:
        '''
        html = self.get_xpath(url)
        if html is not None:
            news_url = html.xpath('//div[@class="news-list"]/ul/li/div[1]/h4/a/@href')
            # print(news_url)
            return news_url


    def write_to_mongo(self,item):
        # 创建新闻id，这个id是通过新闻url获取的hash值
        item['news_id'] = self.get_md5(item['url'])
        self.db['nbanews'].update({'news_id':item['news_id']},{'$set':item},True)
        # print(item)


    def parse_detail(self,url):
        '''
        解析详情页并保存数据
        :param url:
        :return:
        '''
        html = self.get_xpath(url)
        if html is not None:
            # 获取新闻标题
            title = self.get_text(html.xpath('//h1[@class="headline"]/text()'))
            source = self.get_text(html.xpath('//span[@id="source_baidu"]/a/text()'))
            date = self.get_text(html.xpath('//*[@id="pubtime_baidu"]/text()'))
            images = html.xpath('//div[@class="artical-content"]//img/@src')
            content = html.xpath('string(//div[@class="artical-content"])').strip()
            item = {}
            item['title'] = title
            item['source'] = source
            item['date'] = date
            item['images'] = images
            item['content'] = content
            item['url'] = url

            self.write_to_mongo(item)

    def get_md5(self,value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()


    def get_text(self,text):
        # 保证数据的有效性
        if text is not None:
            return text[0]
        else:
            return None


    def main(self):
        while not self.q_page.empty():
            page = self.q_page.get()
            print('-------------第{}页-----------@{}'.format(page,self.name))
            news_url = self.parse_page(self.url % page)
            for url in news_url:
                self.parse_detail(url)


    def run(self):
        self.main()


if __name__ == '__main__':
    base_url = 'http://voice.hupu.com/nba/%s'
    # HupuSipder(base_url)
    # 任务队列中放什么--最顶层的循环条件就是任务队列的内容
    queue_page = Queue()
    for i in range(10, 15):
        queue_page.put(i)
    # 创建线程list，这个list的长度就是线程的数量
    for i in range(4):
        t = HupuSipder(base_url,queue_page)
        t.start()



