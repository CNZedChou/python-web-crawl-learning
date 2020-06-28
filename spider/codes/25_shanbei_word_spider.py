# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  25_shanbei_word_spider.py
@Description    :  
@CreateTime     :  2020-4-29 15:53
------------------------------------
@ModifyTime     :  
"""
import time
import xlwt
import requests
from lxml import etree
def get_xpath(url):
    '''
    请求url，获取页面内容的element对象
    :param url:
    :return: html
    '''
    # 请求url，获得响应
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4121.0 Safari/537.36 Edg/84.0.498.0',

    }
    response = requests.get(url,headers = headers)
    time.sleep(3)
    # 测试请求头是否可以获取数据
    html = etree.HTML(response.text)
    return html


def parse_page(html):
    '''
    解析页面，提取数据
    :param html:
    :return:
    '''
    # 去除所有的tr标签
    tr_list = html.xpath('//tr')
    for tr in tr_list:
        try:
            en_word = tr.xpath('.//strong/text()')[0]
            zh_word = tr.xpath('.//td[@class="span10"]/text()')[0]
            item = {}
            item['English'] = en_word
            item['Chinese'] = zh_word
            word_list.append(item)
        except Exception:
            pass

def main():
    base_url = 'https://www.shanbay.com/wordlist/110521/232414/?page=%s'
    # 刚开始测试最好只写一页
    for i in range(1,4):
        html = get_xpath(base_url % i)
        parse_page(html)
    write_to_excel('word_list.xls','python单词',word_list)


def write_to_excel(filename,sheetname,word_list):
    try:
        # 创建workbook
        workbook = xlwt.Workbook(encoding='utf-8')
        # 给工作表添加sheet表单
        sheet = workbook.add_sheet(sheetname)
        # 设置表头
        head = []
        for k in word_list[0].keys():
            head.append(k)
        # 将表头写入excel
        for i in range(len(head)):
            sheet.write(0,i,head[i])
        # 写内容
        i = 1
        for item in word_list:
            for j in range(len(head)):
                sheet.write(i,j,item[head[j]])
            i += 1
        # 保存
        workbook.save(filename)
        print("写入文件成功")
    except Exception as e:
        print(e)
        print("写入文件失败")


if __name__ == '__main__':
    word_list=[]
    main()