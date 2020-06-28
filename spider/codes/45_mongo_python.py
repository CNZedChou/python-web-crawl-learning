# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  45_mongo_python.py
@Description    :  
@CreateTime     :  2020-5-15 00:51
------------------------------------
@ModifyTime     :  
"""
import pymongo

# 创建连接
client = pymongo.MongoClient()# 默认是localhost 和27017
# 用这个client连接数据库
db = client['shop']
# 使用这个db选择一个集合做crud
people = {'name':'aaa','age':11}
# result = db['goods'].insert(people)
# print(result)# 5ebdf85d5d08dd3364cc597c
# result = db['goods'].find({'name':'aaa'})
# # print(result)#
# # for i in result:
# #     print(i)
# #     print(i['name'])
result = db['goods'].aggregate([{'$match':{'shop_price':{'$gt':50}}},
                       {'$group':{'_id':'cat_id','t':{'$sum':1}}},
                       {'$match':{'t':{'$gt':3}}}])
for i in result:
    print(i)