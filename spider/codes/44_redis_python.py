# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  44_redis_python.py
@Description    :  
@CreateTime     :  2020-5-15 00:42
------------------------------------
@ModifyTime     :  
"""
import redis
# 创建一个redis 连接
re = redis.Redis(host='127.0.0.1' ,port=6379,password=None)
# 通过连接对象来执行相应的redis命令
# re.set('pythonCourse','爬虫') #相当于set pythonCourse 爬虫
# 取list 的内容
result = re.lrange('l1',0,-1)
print(result) # [b'3', b'3', b'2']  b表示redis保存的数据都是bytes类型
# 取hash 表
result = re.hget('a:p1','name')
print(result)# b'aaa'
# 添加集合内容
result = re.sadd('myset1','one')
print(result) # 0表示已经存在