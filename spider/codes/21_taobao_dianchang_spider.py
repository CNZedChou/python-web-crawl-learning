# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  21_taobao_dianchang_spider.py
@Description    :  
@CreateTime     :  2020-4-27 13:20
------------------------------------
@ModifyTime     :  
"""
'''
https://tce.taobao.com/api/mget.htm?callback=jsonp1495&tce_sid=1870256,1870299&tce_vid=0,1&tid=,&tab=,&topic=,&count=,&env=online,online

https://tce.taobao.com/api/mget.htm?callback=jsonp1739&tce_sid=1870333,1871655&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online

https://tce.taobao.com/api/mget.htm?callback=jsonp1826&tce_sid=1870340,1871656&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online

https://tce.taobao.com/api/mget.htm?callback=jsonp2074&tce_sid=1870343,1871658&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online


'''

import requests,re,json

def get_content(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url,headers = headers)
    return response.text


def parse_response(response_str):
    # 第一步使用正则将json数据提取
    p = re.compile(r'{.*}')
    result = p.findall(response_str)[0]
    # 使用json模块解析json
    json_data = json.loads(result)
    infos_dict = json_data['result']
    for k,v in infos_dict.items():
        result = v['result']
        for i in result:
            try:
                # 两个key ，其中每个都有result，通过try方式来获得需要的数据，而不是报错停止
                item = {}
                item['current_price'] = i['item_current_price']
                item['title'] = i['item_title']
                print(item)
            except Exception:
                pass


def main():
    url1 = 'https://tce.taobao.com/api/mget.htm?callback=jsonp1495&tce_sid=1870256,1870299&tce_vid=0,1&tid=,&tab=,&topic=,&count=,&env=online,online'
    url2 = 'https://tce.taobao.com/api/mget.htm?callback=jsonp1739&tce_sid=1870333,1871655&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online'
    url3 = 'https://tce.taobao.com/api/mget.htm?callback=jsonp1826&tce_sid=1870340,1871656&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online'
    url4 = 'https://tce.taobao.com/api/mget.htm?callback=jsonp2074&tce_sid=1870343,1871658&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online'
    url_list = [url1,url2,url3,url4]
    for url in url_list:
        response_str = get_content(url)
        # 解析响应的内容
        parse_response(response_str)


if __name__ == '__main__':
    main()
