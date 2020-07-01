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
class ProxyMetaClass(type):
    """
    设定一个元类：
    1。继承type
    """
    def __new__(cls, name,bases,attrs):
        """
        定义一个属性：__crawlfunc__ = []
        __crawlcount__ = int -- 爬取方法的数量
        :param name: 类的名称
        :param bases: 类的继承元组
        :param attrs: 类的属性字典
        :return:
        """
        __crawlfuncs__ = []
        count = 0
        for k,v in attrs.items():
            if 'crawl_' in k:
                __crawlfuncs__.append(k)
                count+=1
        attrs['__crawlfuncs__'] = __crawlfuncs__
        attrs['__crawlcount__'] = count
        # 最终还是由type来执行的
        # 调用父类的type来创建
        # 父类的type也是通过__new__来创建的
        return type.__new__(cls,name,bases,attrs)
        # return super().__new__(name,bases,attrs)



class FreeProxyGetter(object,metaclass=ProxyMetaClass):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

        }


    def get_proxies(self,crawl_func):
        proxies = []
        # proxies = eval('self.{}()'.format(crawl_func))
        for proxy in eval('self.{}()'.format(crawl_func)):
            proxies.append(proxy)

        return proxies

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
                    # print(ip, port)
                    proxies.append(ip.strip() + ':' + port.strip())
                    yield ip.strip() + ':' + port.strip()
            # print(proxies)

        # return proxies


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
                    # print(ip, port)
                    proxies.append(ip.strip() + ':' + port.strip())
                    yield ip.strip() + ':' + port.strip()
        # return proxies

if __name__ == '__main__':
    f = FreeProxyGetter()
    print(dir(f))