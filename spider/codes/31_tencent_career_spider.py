# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  31_tencent_career_spider.py
@Description    :  
@CreateTime     :  2020-5-3 22:06
------------------------------------
@ModifyTime     :  
"""
from lxml import etree
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from excel_utils.excel_write import ExcelUtils

class TencentCareer(object):
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.filename = '腾讯招聘.xls'
        self.main()

    def main(self):
        for i in range(10):
            html_str = self.get_content_by_selenium(self.url % i)
            html = etree.HTML(html_str)
            div_list = html.xpath('/html/body/div/div[4]/div[3]/div[2]/div[2]/div/div')
            self.parse_div(div_list)
            i += 1

    def get_content_by_selenium(self, url):
        self.driver.get(url)
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[4]/div[3]/div[2]')))
        return self.driver.page_source

    def parse_div(self, div_list):
        '''
        解析div，获取岗位数据
        :param div_list:
        :return:
        '''
        info_list = []
        for div in div_list:
            career_name = div.xpath('.//a/h4/text()')
            career_infos = div.xpath('.//a/p[1]/span/text()')
            career_city = career_infos[1]
            career_type = career_infos[2]
            career_date = career_infos[-1]
            career_description = div.xpath('.//a/p[2]/text()')
            item = {}
            item['career_name'] = career_name
            item['career_city'] = career_city
            item['career_type'] = career_type
            item['career_date'] = career_date
            item['career_description'] = career_description
            info_list.append(item)

        if os.path.exists(self.filename):
            ExcelUtils.write_to_excel_append(self.filename,info_list)
        else:
            ExcelUtils.write_to_excel(self.filename,'tencent career',info_list)


if __name__ == '__main__':
    base_url = 'https://careers.tencent.com/search.html?index=%s'
    TencentCareer(base_url)