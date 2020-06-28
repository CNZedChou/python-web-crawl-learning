# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  04baidu_translator_spider.py
@Description    :  
@CreateTime     :  2020-4-19 23:09
------------------------------------
@ModifyTime     :  
"""
import requests
import json
# 实现翻译任意单词
def translate(kw):
    base_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': kw
    }
    data_len = len(str(data))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://fanyi.baidu.com/',
        'content-length': str(data_len),  # post请求数据的长度的个数（字符的个数）
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
    response = requests.post(base_url,headers = headers,data=data)
    json_data = json.loads(response.text)
    result = ''
    for data in json_data['data']:
        result += data['v'] +'\n'
    return result

if __name__ == '__main__':
    kw = 'word'
    result = translate(kw)
    print(result)