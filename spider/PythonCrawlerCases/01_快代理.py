# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  01_快代理.py
@Description    :  
@CreateTime     :  2020-5-7 12:10
------------------------------------
@ModifyTime     :  
"""
import requests
import parsel
import time
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',

    }
    for i in range(1,5):
        print('正在获取第{}页数据'.format(i))
        response = requests.get(base_url.format(i),headers = headers)
        data = response.text
        # 转换数据类型
        html_data = parsel.Selector(data)
        # 数据解析
        tr_list = html_data.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in tr_list:
            dict_proxies = {}
            proxy_type = tr.xpath('./td[4]/text()').extract_first()
            ip_address = tr.xpath('./td[1]/text()').extract_first()
            ip_port = tr.xpath('./td[2]/text()').extract_first()
            dict_proxies[proxy_type] = ip_address + ':' + ip_port
            proxies_list.append(dict_proxies)
            print(dict_proxies)
            time.sleep(0.5)
        print('获取到的代理ip的数量:',len(proxies_list))
    use_list = check_ip(proxies_list)
    print('能用的ip',use_list)
    print('能用的ip数量:',len(use_list))
def check_ip(proxies_list):
    '''
    检测代理ip的质量
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',

    }
    high_quality = []
    for proxy in proxies_list:
        try:
            response = requests.get('https://www.baidu.com',headers=headers,proxies=proxy,timeout=0.1)
            if response.status_code == 200:
                high_quality.append(proxy)
        except Exception as e:
            print(e)
        finally:
            print('当前ip：',proxy,'检测通过')
    return high_quality
if __name__ == '__main__':
    base_url = 'https://www.kuaidaili.com/free/inha/{}/'
    proxies_list = []
    main()
