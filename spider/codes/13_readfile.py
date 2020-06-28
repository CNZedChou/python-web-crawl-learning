# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  13_readfile.py
@Description    :  
@CreateTime     :  2020-4-25 14:43
------------------------------------
@ModifyTime     :  
"""
fp = open('12_reg_test.py','r',encoding='utf-8')
# enumerate() 可迭代对象，索引的开始值，默认是0
for i,line in enumerate(fp,1):
    print(i,line,sep=':')
