# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  32_tencent_ajax_spider.py
@Description    :  
@CreateTime     :  2020-5-6 18:09
------------------------------------
@ModifyTime     :  
"""
import requests
import os
from excel_utils.excel_write import ExcelUtils


def main():
    # 确定ajax url
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1588759866448&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4131.0 Safari/537.36 Edg/84.0.506.0',

    }
    for i in range(1,10):
        response = requests.get(base_url.format(i),headers = headers)
        json_data = response.json()
        # for data in json_data['Data']['Posts']
        infos = json_data['Data']['Posts']
        if os.path.exists(filename):
            ExcelUtils.write_to_excel_append(filename,infos)
        else:
            ExcelUtils.write_to_excel(filename,'tencent ajax',infos)


if __name__ == '__main__':
    filename = '腾讯招聘ajax.xls'
    main()