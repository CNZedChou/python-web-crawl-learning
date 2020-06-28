# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  05jinshan_translator_spider.py
@Description    :  
@CreateTime     :  2020-4-20 14:01
------------------------------------
@ModifyTime     :  
"""
import requests
import json
def translate(w):
    base_url = 'http://fy.iciba.com/ajax.php?a=fy'
    data = {
        'w': w,
    }
    data_len = len(str(data))
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36 Edg/84.0.488.0',
        'X-Requested-With' : 'XMLHttpRequest',
        'Referer' : 'http://fy.iciba.com/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': str(data_len),
    }
    response = requests.post(base_url,headers = headers,data=data)
    '''
        {
        "status":0,
        "content":{
            "ph_en":"ˈpaɪθən",
            "ph_am":"ˈpaɪθɑn",
            "ph_en_mp3":"http://res.iciba.com/resource/amp3/oxford/0/3f/21/3f21dc676529e37bcfdf04047539d2ef.mp3",
            "ph_am_mp3":"http://res.iciba.com/resource/amp3/1/0/23/ee/23eeeb4347bdd26bfc6b7ee9a3b755dd.mp3",
            "ph_tts_mp3":"http://res-tts.iciba.com/2/3/e/23eeeb4347bdd26bfc6b7ee9a3b755dd.mp3",
            "word_mean":[
                "n. 巨蛇，大蟒;"
            ]
        }
    }
    '''
    # 从中可以看出word_mean 为翻译内容
    json_data = json.loads(response.text)
    result = ''
    for data in json_data['content']['word_mean']:
        result += data + '\n'
    return result

if __name__ == '__main__':
    w = 'father'
    result = translate(w)
    print(result)