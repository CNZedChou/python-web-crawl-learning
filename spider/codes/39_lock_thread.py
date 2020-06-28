# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  39_lock_thread.py
@Description    :  
@CreateTime     :  2020-5-8 15:14
------------------------------------
@ModifyTime     :  
"""
import threading,time
#全局变量
g_num = 0
def w1():
    global g_num
    for i in range(10000000):
        #上锁
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num+=1
            #解锁
            mutex.release()
    print("test1---g_num=%d"%g_num)

def w2():
    global g_num
    for i in range(10000000):
        # 上锁
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num+=1
            # 解锁
            mutex.release()
    print("test2---g_num=%d" % g_num)

if __name__ == "__main__":
    #创建锁
    mutex = threading.Lock()

    t1 = threading.Thread(target=w1)
    t1.start()
    t2 = threading.Thread(target=w2)
    t2.start()