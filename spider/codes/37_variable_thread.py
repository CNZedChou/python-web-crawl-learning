# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  37_variable_thread.py
@Description    :  
@CreateTime     :  2020-5-8 14:21
------------------------------------
@ModifyTime     :  
"""
from threading import Thread
import time
import random
g_num = 100#104--GIL#100

def work1():
    global g_num
    for i in range(3):
        g_num += 1
        time.sleep(random.random())
        print('in work1,gum=%d' % g_num)

def work2():
    global g_num
    for i in range(3):
        g_num += 1
        time.sleep(random.random())
        print('in work2,gum=%d' % g_num)

if __name__ == '__main__':
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    t2.start()
