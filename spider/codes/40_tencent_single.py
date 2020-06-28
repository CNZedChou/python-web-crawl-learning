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
def main():
    driver = webdriver.Chrome()
    for i in range(10):
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

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('程序运行时间：' ,time.time()-start_time)#7.274744749069214