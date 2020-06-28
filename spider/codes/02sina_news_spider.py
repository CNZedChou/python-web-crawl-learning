# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  02sina_news_spider.py
@Description    :  
@CreateTime     :  2020-4-19 17:24
------------------------------------
@ModifyTime     :  
"""
import requests
from urllib import parse

def main(kw):

    base_url = 'https://search.sina.com.cn/?'
    # headers 字典
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0'
    }
    # params 字典
    params = {
        'q': kw,
        'c': 'news',
        'from' : 'channel',
        'ie': 'utf-8'
    }
    url_extend = parse.urlencode(params)
    full_url = base_url + url_extend
    response = requests.get(full_url)
    # print(url_extend)
    with open('sina_news3.html','w',encoding='utf-8') as fp:
        fp.write(response.text)
    # response = requests.get(base_url,headers = headers,params = params)
    # with open('sina_news2.html','w',encoding='gbk') as fp:
    #     fp.write(response.text)

if __name__ == '__main__':
    kw = '春晚'
    main(kw)