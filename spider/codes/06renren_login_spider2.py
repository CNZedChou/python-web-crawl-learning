# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  06renren_login_spider2.py
@Description    :  
@CreateTime     :  2020-4-20 14:44
------------------------------------
@ModifyTime     :  
"""
import requests
'''
使用requests种的session对象，使用用户名登录
'''
def login():
    login_url = 'http://www.renren.com/PLogin.do'
    # 创建一个session对象,使用session对象进行登录操作
    session = requests.session()
    data = {
        'email': '1021844583@qq.com',
        'password' : '15958392088Zed'
    }
    session.post(login_url,headers = headers,data = data)
    return session
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0',

    }
    session = login()
    index_url = 'http://www.renren.com/309870215'
    response = session.get(index_url,headers = headers)
    if '周智豪' in response.text:
        print('登录成功')
    else:
        print('登陆失败')