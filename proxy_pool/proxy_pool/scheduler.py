# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  scheduler.py
@Description    :  校验器，肯定要用到db组件
@CreateTime     :  2020-6-30 13:34
------------------------------------
@ModifyTime     :  
"""
import time
from multiprocessing import Process
from proxy_pool.proxy_pool.db import Redis_Client
import asyncio
import aiohttp
from proxy_pool.proxy_pool.settings import  *
from proxy_pool.proxy_pool.getter import FreeProxyGetter


class VailidtyTester(object):

    def __init__(self):
        self.__raw_proxies=[]
        # self.__conn = Reidis_client()

    #这个方法一旦被调用，校验器要工作了
    def set_raw_proxies(self,proxies):
        self.__raw_proxies=proxies
        self.__conn = Redis_Client()

    #校验代理的逻辑
    #异步模块：aiohttp和asyncio
    async def test_singer_proxy(self,proxy):

        try:
            async with aiohttp.ClientSession() as session:
                # 参数校验
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                # ip:port
                real_proxy = 'http://' + proxy
                try:
                    async with session.get(TEST_API, headers=TEST_HEADERS, proxy=real_proxy, timeout=10) as response:
                        if response.status == 200:
                            # 代理是有效的
                            # 添加到代理池
                            self.__conn.put(proxy)
                            print('有效代理！',proxy)

                except Exception:
                    print('无效代理！',proxy)

        except Exception as e:
            print(e)

    def tester(self):
        print('校验器开始工作！')

        loop = asyncio.get_event_loop()
        #执行方法
        #任务列表
        #从篮子里取出每一个代理，执行上面方法即可
        tasks = [self.test_singer_proxy(x) for x in self.__raw_proxies]
        #监听
        loop.run_until_complete(asyncio.wait(tasks))


class PoolAdder(object):
    def __init__(self,threshold):
        self.__threshold = threshold
        self.__conn = Redis_Client()
        self.__tester = VailidtyTester()
        self.__crawler = FreeProxyGetter()

    # 停止条件
    def is_over_threshold(self):
        """
         # 判断是否超过最大值
        :return: True 超过
        """
        if self.__threshold <= self.__conn.queue_len:
            return True
        else:
            return False


    def add_to_queue(self):
        print('添加器开始工作')
        while True:
            # 超过最大值就停止工作
            if self.is_over_threshold():
                break
            # 1. 调用crawler 获取代理,循环：关键是从哪里获取__crawler的这些爬取代理的方法名
            # 可以使用dir()方法得到属性名，然后选择想要的方法
            # attrs_crawl = dir(self.__crawler)
            # crawl_method = [x for x in attrs_crawl if 'crawl_' in x]
            # proxies = self.__crawler.crawl_ip3366()
            proxies_count = 0
            for crawl_func in self.__crawler.__crawlfuncs__:
                try:
                    # 在底层方法没有进行try catch的处理
                    proxies = self.__crawler.get_proxies(crawl_func)
                except Exception:
                    # 当一个方法不行的时候更换另一个方法
                    continue
            # 2. 调用校验器检验并添加
            self.__tester.set_raw_proxies(proxies)
            self.__tester.tester()
            proxies_count += len(proxies)
            if proxies_count == 0:
                print('代理网站全部失效,请添加新的代理网站获取代理')


class Scheduler(object):
    @staticmethod
    def valid_proxy(cycle = CYCLE_VALID_TIME):
        # 从代理池中取出之前爬取的一半，重新校验
        conn = Redis_Client()
        tester = VailidtyTester()
        while True:
            print('循环校验器开始工作')
            # 取一半的长度
            count = int(conn.queue_len * 0.5)
            if count == 0:
                print("代理池的数量不足，请添加")
                time.sleep(cycle)
            proxies = conn.get(count)
            # 校验
            tester.set_raw_proxies(proxies)
            tester.tester()
            time.sleep(cycle)


    @staticmethod
    def check_pool_add(lower_num = LOWER_NUM,upper_num = UPPER_NUM,cycle = CHECK_POOL_CYCLE):
        conn = Redis_Client()
        adder = PoolAdder(upper_num)
        while True:
            if conn.queue_len < lower_num:
                adder.add_to_queue()
            time.sleep(cycle)



    def run(self):
        valid_process = Process(target=Scheduler.valid_proxy)
        check_process = Process(target=Scheduler.check_pool_add)
        valid_process.start()
        check_process.start()


