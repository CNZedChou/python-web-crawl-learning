# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  33_single_thread.py
@Description    :  
@CreateTime     :  2020-5-7 23:47
------------------------------------
@ModifyTime     :  
"""
import time
import random
'''
单线程程序特点：按照程序的流程执行
'''
def download(fileName):
    print("{}文件开始下载".format(fileName))
    time.sleep(random.random()*10)
    print("{}文件下载完成".format(fileName))


# 单线程 默认主线程
if __name__ == '__main__':
    for i in range(5):
        download(i)

