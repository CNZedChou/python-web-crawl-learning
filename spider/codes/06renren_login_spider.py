# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  06renren_login_spider.py
@Description    :  
@CreateTime     :  2020-4-20 14:35
------------------------------------
@ModifyTime     :  
"""
import requests
'''
用封装cookie的形式来登录
'''
def login():
    base_url = 'http://www.renren.com/974266505'
    headers = {
        'Cookie' : 'anonymid=k983whwzowu6d9; depovince=ZJ; _r01_=1; JSESSIONID=abcufZ5hXyrWzdSuBtwgx; taihe_bi_sdk_uid=64a52d6bcc8697ffd8126f12b189c63b; taihe_bi_sdk_session=193e7413ec8bd6224b795a26805d435e; ick_login=fcc43659-aa12-4741-b3c5-d7e26cd2b835; t=a36ceac04ca5a703d3a6dfbd2b22522c5; societyguester=a36ceac04ca5a703d3a6dfbd2b22522c5; id=974266505; xnsid=69b23064; jebecookies=3a21bf21-f4d7-4a84-ad19-786fa658b0a4|||||; ver=7.0; loginfrom=null; jebe_key=edb7c4a5-2529-4448-bb6e-336db9adb552%7Cfec133727ef4cc78c2e50ae5971b3c15%7C1587364618965%7C1%7C1587364620193; jebe_key=edb7c4a5-2529-4448-bb6e-336db9adb552%7Cfec133727ef4cc78c2e50ae5971b3c15%7C1587364618965%7C1%7C1587364620195; wp_fold=0',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0'
    }
    response = requests.get(base_url,headers = headers)
    if '绸载德' in response.text:
        return True
    else:
        return False

if __name__ == '__main__':
    result = login()
    if result:
        print('登录成功')
    else:
        print('登陆失败')