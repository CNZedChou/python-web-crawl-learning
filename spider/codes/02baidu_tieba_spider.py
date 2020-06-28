# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  02baidu_tieba_spider.py
@Description    :  
@CreateTime     :  2020-4-19 18:52
------------------------------------
@ModifyTime     :  
"""
import requests
import os
def main():
    # 确定基础URL
    base_url = 'https://tieba.baidu.com/f?'
    # 准备参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0'
    }
    filename = './tieba/' + kw
    if not os.path.exists(filename):
        os.mkdir(filename)

    for i in range(10):
        # pn 值为页码值
        pn  = i * 50
        params = {
            'kw': kw,
            'ie': 'utf - 8',
            'tab': 'corearea',
            'pn': pn
        }
        # 发送请求，获取响应
        response = requests.get(base_url,headers = headers,params= params)
        with open(filename + '/'+ str(i + 1) + '.html','w',encoding='utf-8' ) as fp :
            fp.write(response.text)

if __name__ == '__main__':
    kw = '武汉'
    main()