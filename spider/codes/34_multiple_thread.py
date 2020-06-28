# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  34_multiple_thread.py
@Description    :  
@CreateTime     :  2020-5-8 10:56
------------------------------------
@ModifyTime     :  
"""
import threading
import time
import random
def download(fileName):
    print("{}文件开始下载".format(fileName))
    time.sleep(random.random()*10)
    print("{}文件下载完成".format(fileName))

if __name__ == '__main__':
    # 创建5个线程
    for i in range(5):
        t = threading.Thread(target=download,args=(i,))
        t.start()