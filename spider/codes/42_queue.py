# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  42_queue.py
@Description    :  
@CreateTime     :  2020-5-8 16:04
------------------------------------
@ModifyTime     :
"""
from queue import Queue
# 创建一个队列:可以让原本有序的东西，在出队的过程中保持原来的顺序
queue_num = Queue()
for i in range(200):
    # 入队操作
    queue_num.put(i)
# while not queue_num.empty():
#     # 出队
#     print(queue_num.get())
for i in range(1000):
    print(queue_num.get(block=False)) # block = False ，表示get方法为非阻塞方法，当队列为空的时候就抛出异常，
    # block = True 是默认情况，表示方法为阻塞方法，当队列为空，就阻塞当前线程
