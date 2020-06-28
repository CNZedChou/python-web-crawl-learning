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
class MyThread(threading.Thread):
    def __init__(self, fileName,name):
        super().__init__()
        self.name = name
        self.fileName = fileName
    def run(self):
        # print('线程运行中')
        self.download(self.fileName)
    def download(self,fileName):
        print("{}文件开始下载{}".format(fileName,self.name))
        time.sleep(random.random()*10)
        print("{}文件下载完成{}".format(fileName,self.name))

if __name__ == '__main__':
    # 创建5个线程
    name_list = ['a','b','c','d','e']
    for i in range(5):
        t = MyThread(i,name = name_list[i])
        t.start()