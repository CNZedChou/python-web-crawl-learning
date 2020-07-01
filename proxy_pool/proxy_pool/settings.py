# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  settings.py
@Description    :  redis的密码，如果为空则表示没有密码
@CreateTime     :  2020-6-30 11:22
------------------------------------
@ModifyTime     :  
"""
PASSWORD = ''
HOST = 'localhost'
PORT = '6379'
# 代理池的名称
PROXYPOOL = 'proxies'
TEST_API = 'https://www.baidu.com'
TEST_HEADERS ={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
}

# 循环校验时间
CYCLE_VALID_TIME = 60
# 代理池数量的最小值
LOWER_NUM = 10
# 代理池数量的最大值
UPPER_NUM = 100
# 检查时间
CHECK_POOL_CYCLE = 60