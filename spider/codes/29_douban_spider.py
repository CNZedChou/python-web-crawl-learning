# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  29_douban_spider.py
@Description    :  
@CreateTime     :  2020-5-3 12:33
------------------------------------
@ModifyTime     :  
"""
import requests
import time
import os
from excel_utils.excel_write import ExcelUtils
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

class DoubanReader(object):

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome() # 放在这里不会请求一次打开一个浏览器界面
        self.filename = '豆瓣python.xls'
        self.main()


    def main(self):
        # 分页请求
        i = 0
        while True:
            html_str = self.get_content_by_selenium(self.url % (i*15))
            # 页面内容转换成element对象就可以使用xpath获取内容
            html = etree.HTML(html_str)
            div_list = html.xpath('//div[@id="root"]/div/div[2]/div/div/div[position()>1]')
            if not div_list:
                break
            self.parse_div(div_list)
            i += 1


    def parse_div(self,div_list):
        '''
        解析div，获取书籍
        :param div_list:
        :return:
        '''
        info_list = []
        for div in div_list:
            # 异常发生程序终止---当前线程中止
            # 规则：异常必须要处理。
            # 异常时层层抛出的,所以在处理异常的时候，一定要分析好处理的位置，
            # 这样决定了你是否能利用异常做一些程序的附加功能
            # 异常功能：
            try:
                # 书籍名称
                book_title = div.xpath('.//div[@class="title"]/a/text()')[0]
                # print(book_title)
                info = div.xpath('.//div[@class="meta abstract"]/text()')
                # print(info)
                infos = info[0].split(r'/')
                # print(infos)
                # 在爬取数据的时候，分析网站，提取数据的时候，有时候总有特例
                # 作者
                book_actor = infos[0]
                # 出版社
                book_publish = infos[-3]
                # 价格
                book_price = infos[-1]
                # 出版日期
                book_date = infos[-2]
                # 详情页链接
                detail_url = div.xpath('.//div[@class="item-root"]/a/@href')[0]
                item = {}
                item['book_title'] = book_title
                item['book_actor'] = book_actor
                item['book_price'] = book_price
                item['book_publish'] = book_publish
                item['detail_url'] = detail_url
                print(item)
                info_list.append(item)
            except Exception:
                pass
        if os.path.exists(self.filename):
            ExcelUtils.write_to_excel_append(self.filename, info_list)
        else:
            ExcelUtils.write_to_excel(self.filename, 'python书籍', info_list)

    def get_xpath(self,url):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4130.0 Safari/537.36 Edg/84.0.502.0',

            }
            response = requests.get(url,headers = headers)
            time.sleep(2)
            if response.status_code == 200:
                return response.text
            else:
                print('链接错误')


    def get_content_by_selenium(self,url):
        # 第一步，创建驱动

        # 第二步，请求url
        self.driver.get(url)
        # 第三步，等待
        # time.sleep(3)# 强制等待
        # driver.implicitly_wait(10)# 隐式等待，10秒钟还没加载完的话，就会报超时异常
        # 使用显式等待的步骤：
        # 1.创建一个等待对象
        # 20:显示等待的最大时长，20秒还没等到特定元素加载完，就报一个超时异常
        # driver:表示等待对象监听的浏览器
        wait = WebDriverWait(self.driver,20)
        # 2.用wait对象来进行条件判断
        '''
        EC.presence_of_element_located(定位器)
        定位器是一个元组（用什么定位器：id，xpath，css,'相应的语法'）
        '''
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[1]/div')))
        # 第四步，获取页面内容
        return self.driver.page_source


if __name__ == '__main__':
    base_url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=%s'
    DoubanReader(base_url)


