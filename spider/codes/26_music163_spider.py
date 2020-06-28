# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  26_music163_spider.py
@Description    :  
@CreateTime     :  2020-5-1 17:00
------------------------------------
@ModifyTime     :  
"""
import time

import requests
from lxml import etree
from excel_utils.excel_write import ExcelUtils

# 在python3中有一个所有的父类object
# 新式类：object子类，python3里面的类
# 旧式类：不是object子类，python2里面的类
# 在python3中显示继承object其实是为了多个版本兼容
class Music163(object):
    def __init__(self,url):
        self.url = url
        self.main()
    def main(self):
        # 第一步：获取分类歌手列表
        area_singer_list = self.get_singer_list(self.url)
        for area in area_singer_list:
            new_url = 'https://music.163.com/' + area
            # 第二步：获取字母列表
            word_singer_list = self.get_word_list(new_url)
            for word in word_singer_list:
                # 第三步：在字母列表中获取歌手信息
                full_url = 'https://music.163.com/' + word
                self.get_singer_information(full_url)

        ExcelUtils.write_to_excel('Singer_Information.xls','Music163_Singer',singer_list)


    def get_xpath(self,url):
        # 准备参数
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4123.0 Safari/537.36 Edg/84.0.499.0',

        }
        response = requests.get(url,headers = headers)
        time.sleep(1)
        if response.status_code == 200:
            return etree.HTML(response.text)
        else:
            print("status wrong")

    def get_singer_list(self, url):
        html = self.get_xpath(url)
        area_list = html.xpath('//div[@id="singer-cat-nav"]/div/ul/li/a/@href')
        return area_list

    def get_word_list(self, new_url):
        word_list_html = self.get_xpath(new_url)
        word_singer_list = word_list_html.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')
        return word_singer_list

    def get_singer_information(self, full_url):
        singer_html = self.get_xpath(full_url)
        li_list = singer_html.xpath('//ul[@id="m-artist-box"]/li')
        for li in li_list:
            # | 在xpath中表示左边右边都要
            try:
                singer_name = li.xpath('.//p/a[1]/text()|./a/text()')[0]
                singer_url = li.xpath('.//p/a[1]/@href|./a/@href')[0]
                item = {}
                item['singer_name'] = singer_name
                item['singer_url'] = full_url+singer_url
                singer_list.append(item)
                print(item)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    # 确定url
    # 在url中，如果有锚点的话要注意
    base_url = 'https://music.163.com/discover/artist/'
    singer_list=[]
    Music163(base_url)
