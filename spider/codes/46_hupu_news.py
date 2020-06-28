# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  46_hupu_news.py
@Description    :  
@CreateTime     :  2020-6-28 11:35
------------------------------------
@ModifyTime     :  
"""
import hashlib
import requests
from lxml import etree
import pymongo

def get_xpath(url):
    ''''
    请求url，获取页面内容的element对象
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4178.0 Safari/537.36 Edg/85.0.558.0',
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return etree.HTML(response.text)
    else:
        return None


def parse_page(url):
    '''
    解析每一个分页，获取列表页url
    :param url:
    :return:
    '''
    html = get_xpath(url)
    if html is not None:
        news_url = html.xpath('//div[@class="news-list"]/ul/li/div[1]/h4/a/@href')
        # print(news_url)
        return news_url


def write_to_mongo(item):
    # 创建新闻id，这个id是通过新闻url获取的hash值
    item['news_id'] = get_md5(item['url'])
    db['nbanews'].update({'news_id':item['news_id']},{'$set':item},True)
    print(item)


def parse_detail(url):
    '''
    解析详情页并保存数据
    :param url:
    :return:
    '''
    html = get_xpath(url)
    if html is not None:
        # 获取新闻标题
        title = get_text(html.xpath('//h1[@class="headline"]/text()'))
        source = get_text(html.xpath('//span[@id="source_baidu"]/a/text()'))
        date = get_text(html.xpath('//*[@id="pubtime_baidu"]/text()'))
        images = html.xpath('//div[@class="artical-content"]//img/@src')
        content = html.xpath('string(//div[@class="artical-content"])').strip()
        item = {}
        item['title'] = title
        item['source'] = source
        item['date'] = date
        item['images'] = images
        item['content'] = content
        item['url'] = url

        write_to_mongo(item)

def get_md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def get_text(text):
    # 保证数据的有效性
    if text is not None:
        return text[0]
    else:
        return None


def main():
    base_url = 'http://voice.hupu.com/nba/%s'
    for i in range(1,10):
        # 第一步：获取每一页的新闻的urls
        news_url = parse_page(base_url % i)
        # 第二部：进入详情页
        for url in news_url:
            parse_detail(url)
        # 第三步：解析保存

if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client['hupu']
    main()

