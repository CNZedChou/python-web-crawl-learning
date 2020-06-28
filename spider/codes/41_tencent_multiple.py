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
def parse_page(i):
    driver = webdriver.Chrome()
    driver.get('https://careers.tencent.com/search.html?index={}&keyword=python'.format(i))
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
        print(item)
def main():
    crawl_list = []
    for i in range(10):
        # 创建一个线程
        t = threading.Thread(target=parse_page,args=(i,))
        t.start()
        crawl_list.append(t)
    for t in crawl_list:
        # join方法的作用就是阻塞当前线程，直到t执行完毕
        t.join()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('程序运行时间：' ,time.time()-start_time)#7.274744749069214