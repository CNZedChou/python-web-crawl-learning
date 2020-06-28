# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  07gaodemap_weather_spider.py
@Description    :  
@CreateTime     :  2020-4-20 17:08
------------------------------------
@ModifyTime     :  
"""
import requests
import time
def getCityCode():
    # 获取城市的adcode
    city_codes = []
    base_url = 'https://ditu.amap.com/service/cityList'
    response = requests.get(base_url,headers = headers)
    #解析json数据
    json_data = response.json()
    for data in json_data['data']['cityData']['hotCitys']:
        city_codes.append((data['adcode'],data['name']))
    for data in json_data['data']['cityData']['otherCitys']:
        city_codes.append((data['adcode'],data['name']))
    return city_codes

def getWeather(adcode,city_name):
    # 获取城市的天气
    base_url = 'https://ditu.amap.com/service/weather?adcode={}'.format(adcode)
    response = requests.get(base_url,headers = headers)
    time.sleep(2) # 睡2秒
    json_data = response.json()
    # 第一条为全国信息，false
    if json_data['data']['result'] == 'true':
        weather_name = json_data['data']['data'][0]['forecast_data'][0]['weather_name']
        max_temp = json_data['data']['data'][0]['forecast_data'][0]['max_temp']
        min_temp = json_data['data']['data'][0]['forecast_data'][0]['min_temp']
        # print(weather_name,max_temp,min_temp)
        item = {}
        item['城市'] = city_name
        item['温度'] = '{}/{}℃'.format(min_temp,max_temp)
        item['天气'] = weather_name
        print(item)

def main():
    city_codes = getCityCode()
    for info in city_codes:
        adcode = info[0]
        city_name = info[1]
        getWeather(adcode,city_name)

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    main()