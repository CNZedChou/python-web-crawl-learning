# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  43_producer_consumer_tencent.py
@Description    :  
@CreateTime     :  2020-5-8 23:17
------------------------------------
@ModifyTime     :  
"""
from queue import Queue
from selenium import webdriver
from lxml import etree
import threading
'''
生产者生产每一页html页面，生产者负责请求---class Producer
消费者消费html，消费者负责解析---class Consumer
缓冲区：队列
'''
class Producer(threading.Thread):
    def __init__(self, url,queue_page,name):
        super().__init__()
        self.url = url
        self.queue_page = queue_page
        self.name = name


    def run(self):
        while True:
            if self.queue_page.empty():
                break
            page = self.queue_page.get()
            html_str = self.get_html(page)
            print("====Producer 第{}页===线程：{}".format(page,self.name))
            # 将生产的数据放入公共缓冲队列

            queue_html.put((page,html_str))

    def get_html(self,i):
        '''
        获取一页页面内容
        :param i: 页码
        :return: 页面字符串内容
        '''
        driver = webdriver.PhantomJS()
        driver.get(self.url.format(i))
        return driver.page_source


class Consumer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name


    def run(self):
        while True:
            # 跳出循环的条拣:保证生产者都不工作，同时缓冲区没东西，消费者才停止消费
            # 缓冲区为空，并且生产者生产完成
            if queue_html.empty() and flag:
                break
            try:
                page,html_str = queue_html.get(block=False)
                self.parse_html(html_str)
                print('第{}页解析成功---线程{}'.format(page,self.name))
            except Exception as e:
                # print("队列为空")
                pass


    def parse_html(self,html_str):
        tree = etree.HTML(html_str)
        div_list = tree.xpath('//div[@class="recruit-list"]')

        for div in div_list:
            ##提取
            title = div.xpath('./a/h4/text()')[0]
            type_ = div.xpath('./a/p/span[1]/text()')
            place = div.xpath('./a/p/span[2]/text()')
            class_job = div.xpath('./a/p/span[3]/text()')
            time1 = div.xpath('./a/p/span[4]/text()')
            responsibility = div.xpath('.//p[@class="recruit-text"]/text()')
            item = {}
            item['title'] = title
            item['type'] = type_
            item['place'] = place
            item['class_job'] = class_job
            item['time1'] = time1
            item['responsibility'] = responsibility
            # print(title)
            # print(item)

if __name__ == '__main__':
    # 创建一个队列：公告缓冲区
    queue_html = Queue()
    # 设置生产方式，创建三个线程去生产,需要将生产者变为线程类；设置消费方式，创建4个线程进行消费，将消费者转换为线程类
    # 轮询参数,False表示生产者没有生产完成
    flag = False
    # 创建生产者的任务队列
    queue_page = Queue()
    for i in range(10):
        queue_page.put(i)
    base_url = 'https://careers.tencent.com/search.html?index={}&keyword=python'
    crawl_list_producer = ['pa', 'pb', 'pc']
    producer_thread_list = []
    for crawl in crawl_list_producer:
        t = Producer(base_url,queue_page,crawl)
        t.start()
        producer_thread_list.append(t)
    crawl_list_consumer = ['c1', 'c2', 'c3', 'c4']
    for crawl in crawl_list_consumer:
        t = Consumer(crawl)
        t.start()
    # 将生产者都加入阻塞可以判断生产者生产是否完成
    for producer in producer_thread_list:
        producer.join()
    flag = True