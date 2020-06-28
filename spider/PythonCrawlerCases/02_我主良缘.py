# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  02_我主良缘.py
@Description    :  
@CreateTime     :  2020-5-7 13:14
------------------------------------
@ModifyTime     :  
"""
import time

import requests
import os

def save_image(item):
    if not os.path.exists('images'):
        os.mkdir('images')
    image_url = item['avatar']
    response = requests.get(image_url)
    if response.status_code == 200:
        file_path = 'images/{}.jpg'.format(item['username'])
        if not os.path.exists(file_path):
            print('正在获取：%s的信息'%item['username'])
            with open(file_path,'wb') as f:
                f.write(response.content)
        else:
            print('已经下载过')


def main():
    startage = 21
    endage = 30
    startheight = 161
    endheight = 170
    for i in range(1,5):
        json_data = get_content(startage,endage,startheight,endheight,i)
        # print(json_data)
        for item in json_data['data']['list']:
            # print(item)
            save_image(item)


def get_content(startage,endage,startheight,endheight,page):
    headers = {
        'Referer': 'http://www.lovewzly.com/jiaoyou.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',

    }
    base_url = 'http://www.lovewzly.com/api/user/pc/list/search?startage={}&endage={}&gender=2&cityid=383&startheight={}&endheight={}&marry=1&education=40&page={}'.format(startage,endage,startheight,endheight,page)
    while True:
        try:
            response = requests.get(base_url,headers = headers)
            time.sleep(1)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()