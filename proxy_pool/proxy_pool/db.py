# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  db.py
@Description    :  db.py 主要从来操作redis
@CreateTime     :  2020-6-30 11:19
------------------------------------
@ModifyTime     :  
"""
from proxy_pool.proxy_pool.settings import *
import redis



class Redis_Client(object):
    def __init__(self):
        """
        考虑到是否有密码
        """
        if PASSWORD is not None:
            self.__db = redis.Redis(host=HOST,port=PORT,password=PASSWORD)
        else:
            self.__db = redis.Redis(host=HOST,port=PORT)

    def put(self,proxy):
        """
        添加一个代理到代理池
        :return:
        """
        self.__db.rpush(PROXYPOOL,proxy)

    def get(self,count = 1):
        """
        获取count个代理，默认为1个
        :return:
        """
        proxies = self.__db.lrange(PROXYPOOL,0,count-1)
        self.__db.ltrim(PROXYPOOL,count,-1)
        return proxies


    def pop(self):
        # redis中存储的是bytes，用的时候必须是字符串
        return self.__db.rpop(PROXYPOOL).decode('utf-8')


    @property
    def queue_len(self):
        # 使得可以用client.queue_len直接调用
        return self.__db.llen(PROXYPOOL)


if __name__ == '__main__':
    redis_client = Redis_Client()
    print(redis_client.queue_len)