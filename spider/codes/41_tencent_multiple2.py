# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  40_tencent_single.py
@Description    :  
@CreateTime     :  2020-5-8 15:46
------------------------------------
@ModifyTime     :  
"""
from selenium import webdriver
from lxml import etree
import time
import threading
from queue import Queue
class Tencent(threading.Thread):
    def __init__(self, url,queue_page,name):
        super().__init__()
        self.url = url
        self.queue_page = queue_page
        self.name = name
    def run(self):
        # 一个类就是一个线程，4个线程，做20个任务，每个线程做多件事情
        # 重复不断地做：从队列中取出一个页码，爬取信息
        while True:
            if self.queue_page.empty():
                break
            page = self.queue_page.get()
            print("第{}页，线程{}".format(page,self.name))
            self.parse(page)


    def parse(self,i):
        driver = webdriver.PhantomJS()
        driver.get(self.url.format(i))
        tree = etree.HTML(driver.page_source)

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
            print(title)
            # print(item)


if __name__ == '__main__':
    start_time = time.time()
    # 第一步：创建任务队列
    base_url = 'https://careers.tencent.com/search.html?index={}&keyword=python'
    queue_page = Queue()
    for i in range(20):
        queue_page.put(i)
    # 第二步：创建线程list，这个list长度是线程的数量
    crawl_list = ['aa','bb','cc','dd']
    thread_list = []
    for crawl in crawl_list:
        # 创建线程
        # queue_page:将创建好的队列传进去
        t = Tencent(base_url,queue_page,crawl)
        t.start()
        thread_list.append(t)
    # 阻塞主线程，保证每个都执行完毕之后来测试程序运行时间
    for t in thread_list:
        t.join()
    print('程序运行时间：', time.time() - start_time)


