# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  38_list_thread.py
@Description    :  
@CreateTime     :  2020-5-8 14:35
------------------------------------
@ModifyTime     :  
"""
import threading
import time
import copy

'''
当列表作为线程任务函数参数,如果对列表做一些更改，需要拷贝一份作为遍历的内容
'''
def work1(download_list,finish_list):
    copy_list = copy.copy(download_list)
    for file in copy_list:
        '''
            #[11,22,33]---download_list[0]--11
            #[22,33]---download_list[1]---33
            #[22]---download_list[2]
        #
        '''
        print("----in work1---download:%d"%file)
        time.sleep(1)
        #下载完成之后
        #1、任务列表中移除已经下载的元素
        download_list.remove(file)
        finish_list.append(file)


if __name__ == '__main__':
    #下载任务列表
    download_list = [11,22,33]
    total = len(download_list)  #总任务列数
    finish_list = []
    t1 = threading.Thread(target=work1,args=(download_list,finish_list))
    t1.start()
    while True:
        print(download_list,finish_list)
        pro = len(finish_list)/total
        print("当前下载进度：%.2f%%"%(pro*100),threading.enumerate())
        time.sleep(1)
        if pro == 1:
            print("全部任务下载完成！")
            break