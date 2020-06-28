# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  30_douban_movie_spider.py
@Description    :  
@CreateTime     :  2020-5-3 13:54
------------------------------------
@ModifyTime     :  
"""
import json
import re
from urllib import parse
import os
import requests
from lxml import etree
from excel_utils.excel_write import ExcelUtils

def get_content(url, headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text


def parse_json(json_data):
    for data in json_data:
        # print(type(data))
        rating = data['rating']
        imag = data['cover_url']
        title = data['title']
        actors = data['actors']
        detail_url = data['url']
        vote_count = data['vote_count']
        types = data['types']
        item = {}
        item['rating'] = rating
        item['imag'] = imag
        item['title'] = title
        item['actors'] = actors
        item['vote_count'] = vote_count
        item['detail_url'] = detail_url
        item['types'] = types
        print(item)
        # movie_list.append(item)
    # if os.path.exists(filename):
    #     ExcelUtils.write_to_excel_append(filename,movie_list)
    # else:
    #     ExcelUtils.write_to_excel(filename,'movie',movie_list)
def parse_ajax(url, type_, refer):
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',
        'Referer':refer
    }
    i = 0
    while True:
        json_str = get_content(url.format(type_,i) ,headers =headers )
        if json_str =='[]':
            break

        json_data = json.loads(json_str)
        # json_data = json_str.json()
        parse_json(json_data)
        i += 100


def main():
    #先请求首页，获取分类
    base_url = 'https://movie.douban.com/chart'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',
        'Referer': 'https://movie.douban.com/',
    }
    html_str = get_content(base_url,headers)
    html = etree.HTML(html_str)
    # 找到分类
    type_link = html.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/a/@href')
    for url in type_link:
        # '/typerank?type_name=剧情&type=11&interval_id=100:90&action='
        p = re.compile(r'.*?type_name=(.*?)&type=(.*?)&interval.*?')
        result = p.search(url)
        type_name = result.group(1)
        type_ = result.group(2)
        params = {
            'type_name': type_name,
            'type': type_,
            'interval_id': '100:90',
            'action': '',
        }
        # parse.urlencode()方法可以将一个字典，装化成key1=value1&key2=value2
        # 同时还能将中文按urlencoding编码来进行转码。
        refer = 'https://movie.douban.com/j/chart/top_list?'+parse.urlencode(params)
        ajax_url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=100'
        parse_ajax(ajax_url, type_, refer)


if __name__ == '__main__':
    filename = '豆瓣电影.xls'
    movie_list = []
    main()