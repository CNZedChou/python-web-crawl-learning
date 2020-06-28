# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  01baidu_spider.py
@Description    :  
@CreateTime     :  2020-4-18 21:23
------------------------------------
@ModifyTime     :  
"""
# 导包
import requests
# 确定待爬取的url
base_url = 'https://www.baidu.com/more/'
# 发送请求，获取相应
response = requests.get(base_url)
# print(response)
# 字符串响应正文
# print(response.text)
response_str = response.content.decode('utf-8')
response.encoding = 'utf-8'
print(response.text)
# print(response.content.decode(response_str))
# with open('index.html','w',encoding='utf-8') as fp:
#    fp.write(response_str)