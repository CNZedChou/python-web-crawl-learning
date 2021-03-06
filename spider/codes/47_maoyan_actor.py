# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  47_maoyan_actor.py
@Description    :  
@CreateTime     :  2020-6-28 17:10
------------------------------------
@ModifyTime     :  
"""
import time

import requests
from lxml import etree
from queue import Queue
from selenium import webdriver
'''
1.爬取策略：从一个明星的相关人那里去找下一个演员
2.如何爬取更多：设置初始任务池--池里可以放：港台，大陆等
3.必须要去重，否则会进入死循环
'''


def get_xpath(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',

    }
    # driver.get(url)
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        print(response.text)
        return etree.HTML(response.text)
    else:
        print(response.status_code)
        return None
    # print(driver.page_source)
    # return driver.page_source

def parse_actor(html):
    """
    解析页面
    :param html:
    :return:返回相关演员
    """
    # 获取中文名
    
    china_name = html.xpath('/html/body/div[3]/div/div[2]/div[1]/p[1]/text()')
    print(china_name)
    # 获取英文名
    # en_name = get_text(html.xpath('//p[@class="eng-name cele-name"]/text()'))
    # 获取职业名
    # profession = get_text(html.xpath('//span[@class="profession"]/text()'))
    # 获取出生日期
    # birthday = get_text(html.xpath('//span[@class="birthday"]/text()'))
    # 获取身高
    # height = get_text(html.xpath('//span[@class="height"]/text()'))
    # 获取代表作
    # master_works = html.xpath('//ul[@class="master-item"]/li/a/img/@alt')
    # print(master_works)

def get_text(text):
    if text is not None:
        return text[0]
    else:
        return None


def url_seen(url):
    """
    判断url是否重复
    :param url:
    :return: True 重复；False 不重复
    """



def main():

    while not q_actor.empty():
        html = get_xpath(q_actor.get())
        # 提取信息保存，获取相关人返回
        time.sleep(10)
        # driver.implicitly_wait(10)
        related_actor_urls = parse_actor(html)
        if related_actor_urls is not None:
            for url in related_actor_urls:
                # 去重判断
                if not url_seen(url):

                # 没有被爬取过
                    q_actor.put(url)


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # start_urls
    actor_url = ['https://maoyan.com/films/celebrity/789',# 成龙
                 # 'https://maoyan.com/films/celebrity/3718', # 安妮海瑟薇
                 # 'https://maoyan.com/films/celebrity/28427', # 周杰伦
                 # 'https://maoyan.com/films/celebrity/31444', # 宫崎骏
                 # 'https://maoyan.com/films/celebrity/8681', # 马东锡
                 ]
    # 调度器
    q_actor = Queue()
    #
    for url in actor_url:
        q_actor.put(url)

    main()


