# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  27_shici_spider.py
@Description    :  
@CreateTime     :  2020-5-2 12:49
------------------------------------
@ModifyTime     :  
"""
import time
import requests
from lxml import etree

class Gushici(object):
    def __init__(self,url):
        self.url = url
        self.main()


    def main(self):
        area_list = self.get_area_gushici(self.url)
        for area in area_list:
            shici_list = self.get_shci_list(area)
            for shici in shici_list:
                self.get_shici_information(shici)
                print(shici_info)


    def get_xpath(self,url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4123.0 Safari/537.36 Edg/84.0.499.0',

        }
        response = requests.get(url,headers = headers)
        time.sleep(2)
        if response.status_code == 200:
            return etree.HTML(response.text)


    def get_area_gushici(self, url):
        html = self.get_xpath(url)
        area_list = html.xpath('.//div[@class="main3"]/div[@class="right"]/div[1]/div[@class="cont"]/a/@href')
        return area_list


    def get_shci_list(self, area):
        html = self.get_xpath(area)
        shici_list = html.xpath('.//div[@class="main3"]/div[@class="left"]/div[2]/div[@class="typecont"]/span/a/@href')
        return shici_list


    def get_shici_information(self, shici):
        html = self.get_xpath(shici)
        shici_name = html.xpath('.//div[@class="main3"]/div[@class="left"]/div[2]/div[@class="cont"]/h1/text()')
        shici_dynasty = html.xpath('.//div[@class="main3"]/div[@class="left"]/div[2]/div[@class="cont"]/p/a[1]/text()')
        shici_author = html.xpath('.//div[@class="main3"]/div[@class="left"]/div[2]/div[@class="cont"]/p/a[2]/text()')
        shici_content = html.xpath('.//div[@class="main3"]/div[@class="left"]/div[2]/div[@class="cont"]/div[@class="contson"]/text()')
        item={}
        item['shici_name'] = shici_name
        item['shici_dynasty'] = shici_dynasty
        item['shici_author'] = shici_author
        item['shici_content'] = shici_content
        shici_info.append(item)


if __name__ == '__main__':
    base_url = 'https://www.gushiwen.org/'
    shici_info = []
    Gushici(base_url)