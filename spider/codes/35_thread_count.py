# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  35_thread_count.py
@Description    :  
@CreateTime     :  2020-5-8 13:10
------------------------------------
@ModifyTime     :  
"""
import threading
import time
import random

def sing():
    for i in range(3):
        print("正在唱歌。。。。{}".format(i))
        time.sleep(random.random())

def dance():
    for i in range(3):
        print("正在跳舞。。。。{}".format(i))
        time.sleep(random.random())

#主线程代码：
if __name__ == '__main__':
    #打印晚会开始时间（可读）
    print('晚会开始：{}'.format(time.ctime()))
    #分别创建执行sing和dance函数的线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    #主线程
    t1.start()
    t2.start()
    # 主线程不终止
    while True:
        # 查看线程数量（包括主线程，至少含有一个主线程）
        length = len(threading.enumerate())
        # 主线程加上两个子线程的线程，一共三个线程
        print('当前运行的线程数为：{}'.format(length))
        time.sleep(0.1)
        if length <= 1:
            break
