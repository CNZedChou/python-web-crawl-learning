# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  22_guba_spider.py
@Description    :  
@CreateTime     :  2020-4-28 13:46
------------------------------------
@ModifyTime     :  
"""
import requests, re, json, time


def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4121.0 Safari/537.36 Edg/84.0.495.0',

    }
    response = requests.get(url, headers=headers)
    time.sleep(3)
    if response.status_code == 200:
        return response.text


def parse_html(html_str):
    balist_p = re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>', re.S)
    balist = balist_p.search(html_str).group()
    li_p = re.compile(r'<li>(.*?)</li>', re.S)
    li_list = li_p.findall(balist)
    for li in li_list:
        # 阅读量
        read_p = re.compile(r'<cite>(.*?)</cite>', re.S)
        read = read_p.search(li).group(1).strip()
        # 评论
        comment_p = re.compile(r'</cite>.*<cite>(.*?)</cite>', re.S)
        comment = comment_p.search(li).group(1).strip()
        # 标题
        title_p = re.compile(r'class="note">(.*?)</a>', re.S)
        title = title_p.search(li).group(1).strip()
        # 作者
        author_p = re.compile(r'target="_blank"><font>(.*?)</font></a>', re.S)
        author = author_p.search(li).group(1).strip()
        # 时间
        date_p = re.compile(r'<cite class="last">(.*?)</cite>', re.S)
        date = date_p.search(li).group(1).strip()
        item = {}
        item['read'] = read
        item['comment'] = comment
        item['title'] = title
        item['author'] = author
        item['date'] = date
        guba_list.append(item)


def write_to_json(item):
    with open('guba_spider_infos.json', 'w', encoding='utf-8') as fp:
        json.dump(item, fp)
    print('写入成功')


def main():
    base_url = 'http://guba.eastmoney.com/default,99_%s.html'
    for i in range(1, 13):
        html_str = get_content(base_url % i)
        parse_html(html_str)
    write_to_json(guba_list)


if __name__ == '__main__':
    guba_list = []
    main()
