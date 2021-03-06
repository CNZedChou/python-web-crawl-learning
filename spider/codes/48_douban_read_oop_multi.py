# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  48_douban_read.py
@Description    :  
@CreateTime     :  2020-6-29 10:14
------------------------------------
@ModifyTime     :  
"""
import requests
import re
import json
from selenium import webdriver
from lxml import etree
import hashlib
import pymongo
import threading
from queue import Queue


class DoubanRead(threading.Thread):
    def __init__(self, q_params=None):
        super().__init__()

        self.client = pymongo.MongoClient()
        self.db = self.client['douban_read']
        self.q_params = q_params
        # self.run()

    def get_content_by_selenium(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(3)
        html_str = driver.page_source
        driver.quit()
        return etree.HTML(html_str)

    def get_content_by_requests(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4178.0 Safari/537.36 Edg/85.0.558.0',

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_text(self, text):
        if text is not None:
            return text[0]
        else:
            return ''

    def handle_number(self, text):
        """
        处理带逗号的字符串数字
        :param text:
        :return:
        """
        p = re.compile(r'\d+')
        result = p.findall(text)
        return ''.join(result)

    def get_md5(self, value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()

    def write_to_mongo(self, item):
        item['book_id'] = self.get_md5(item['book_url'])
        self.db['book'].update({'book_id': item['book_id']}, {'$set': item}, True)
        print(item)

    def parse_detail(self, item):
        book_url = item['book_url']
        html_str = self.get_content_by_requests(book_url)
        html = etree.HTML(html_str)
        try:
            desc = html.xpath('string(//div[@class="when-expand"]/p/text()|//div[@class="when-fold"]/text())')
            # 阅读数
            read_num = html.xpath('//div[@class="count-group"]/span[2]/div[2]/text()')[0]
            # 收藏数
            collect_num = html.xpath('//div[@class="count-group"]/span[3]/div[2]/text()')[0]
            # 月票数
            monthly_ticket = html.xpath('//div[@class="count-group"]/span[4]/div[2]/text()')[0]
            # 累计推荐数
            total_ticket = html.xpath('//div[@class="count-group"]/span[5]/div[2]/text()')[0]
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = self.handle_number(collect_num)
            item['monthly_ticket'] = self.handle_number(monthly_ticket)
            item['total_ticket'] = self.handle_number(total_ticket)
        except Exception:
            desc = html.xpath('string(//div[@class="info"])')
            # 阅读数
            read_num = self.get_text(html.xpath('//span[@class="read-count"]/text()'))
            collect_num = ''
            monthly_ticket = ''
            total_ticket = ''
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = collect_num
            item['monthly_ticket'] = monthly_ticket
            item['total_ticket'] = total_ticket
        self.write_to_mongo(item)

    def parse_ajax(self, read_type, read_index):
        """
        获取每个分类的ajax数据
        :param read_type: 请求url中的type内容
        :param read_index: 请求url中的index内容
        :return:
        """
        ajax_url = 'https://read.douban.com/j/index//charts?type={}&index={}&verbose=1'.format(read_type, read_index)
        json_str = self.get_content_by_requests(ajax_url)
        # print(json_data)
        json_data = json.loads(json_str)
        if json_data is not None:
            for data in json_data['list']:
                title = data['works']['title']
                book_url = 'https://read.douban.com' + data['works']['url']
                author = data['works']['author'][0]['name']
                wordCount = data['works']['wordCount']
                item = {}
                item['title'] = title
                item['book_url'] = book_url
                item['author'] = author
                item['wordCount'] = wordCount
                # print(item)
                self.parse_detail(item)

    def get_params(self):
        """
        获取队列的参数
        :return: list 中 包含type 和 index
        """
        params = []
        base_url = 'https://read.douban.com/charts'
        html = self.get_content_by_selenium(base_url)
        type_urls = html.xpath('//div[@class="rankings-nav"]/a[position()>1]/@href')
        # print(type_urls)
        for url in type_urls:
            # 使用正则提取数据
            # '/charts?type=unfinished_column&index=featured&dcs=charts&dcm=charts-nav'
            p = re.compile(r'type=(.*?)&index=(.*?)&dcs')  # 提取到的部分就是type的内容和index的内容
            read_type = p.search(url).group(1)
            read_index = p.search(url).group(2)
            # print(read_type,read_index)
            # cls.parse_ajax(read_type, read_index)
            # 使用元组来接收数据
            params.append((read_type, read_index))
        return params

    def run(self):
        while not self.q_params.empty():
            # 不能写为self.parse_ajax(self.q_params.get()[0],self.q_params.get()[1])
            rtype, rindex = q_params.get()
            self.parse_ajax(rtype, rindex)


if __name__ == '__main__':
    """
    任务队列里面放啥，线程就做啥
    最顶层：最顶层的多个条件
    """
    q_params = Queue()
    douban = DoubanRead()
    params = douban.get_params()
    for info in params:
        q_params.put(info)
    for i in range(4):
        t = DoubanRead(q_params)
        t.start()
