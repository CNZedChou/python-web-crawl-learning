# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  getter.py
@Description    :  爬取免费代理ip
@CreateTime     :  2020-6-30 13:30
------------------------------------
@ModifyTime     :  
"""
import requests
from lxml import etree


class FreeProxyGetter(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

        }

    def crawl_66ip(self):
        # global headers
        """
        url:http://www.66ip.cn/
        :return:list[proxy]
        """
        proxies = []
        base_url = 'http://www.66ip.cn/%s.html'
        for i in range(1, 20):
            response = requests.get(base_url % i, headers=self.headers)
            html = etree.HTML(response.text)
            ips = html.xpath('//tr[position()>1]/td[1]/text()')
            ports = html.xpath('//tr[position()>1]/td[2]/text()')
            if len(ips) == len(ports) and ips is not None and ports is not None:
                for j, ip in enumerate(ips):
                    port = ports[j]
                    print(ip, port)
                    proxies.append(ip.strip() + ':' + port.strip())
            print(proxies)

        return proxies


    def crawl_ip3366(self):
        """
            url:http://www.ip3366.net/?stype=1&page=1
            :return:list[proxy]
        """
        # global headers
        proxies = []
        base_url = 'http://www.ip3366.net/?stype=1&page=%s'
        for i in range(1, 11):
            response = requests.get(base_url % i, headers=self.headers)
            html = etree.HTML(response.text)
            ips = html.xpath('//tr/td[1]/text()')
            ports = html.xpath('//tr/td[2]/text()')
            if not (not (len(ips) == len(ports)) or not (ips is not None) or not (ports is not None)):
                for j, ip in enumerate(ips):
                    port = ports[j]
                    print(ip, port)
                    proxies.append(ip.strip() + ':' + port.strip())
                    # yield ip.strip() + ':' + port.strip()
        return proxies