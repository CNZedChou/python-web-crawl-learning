# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  36_thread_order.py
@Description    :  
@CreateTime     :  2020-5-8 13:51
------------------------------------
@ModifyTime     :  
"""
import threading
import time
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + "@"+str(i)
            print(msg)
            time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
