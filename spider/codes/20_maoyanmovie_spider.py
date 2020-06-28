# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  20_maoyanmovie_spider.py
@Description    :  
@CreateTime     :  2020-4-25 21:38
------------------------------------
@ModifyTime     :  
"""
import requests,re,json,time
def get_content(url):
    # 请求给定url的页面，返回页面内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4121.0 Safari/537.36 Edg/84.0.495.0',

    }
    response = requests.get(url, headers=headers)
    time.sleep(3)
    if response.status_code == 200:
        # 请求成功
        return response.text


def parse_html(html_str):
    # 从页面的str中使用正则提取信息
    # 电影名称，演员，上映时间，评分，详情页链接
    dl_p = re.compile(r'<dl class="board-wrapper">.*?</dl>',re.S) #re.S 是为了匹配换行符
    dl_content = dl_p.search(html_str).group()
    ## 获取每一个dd标签
    dd_p = re.compile(r'<dd>.*?</dd>',re.S)
    dd_list = dd_p.findall(dl_content)
    for dd in dd_list:
        # 电影名称
        movie_title_p = re.compile(r'title="(.*?)" class="image-link',re.S)
        movie_title = movie_title_p.search(dd).group(1)
        # 演员
        movie_actor_p = re.compile(r'<p class="star">(.*?)</p>',re.S)
        movie_actor = movie_actor_p.search(dd).group(1).strip()
        # 上映时间
        movie_date_p = re.compile(r'<p class="releasetime">(.*?)</p>',re.S)
        movie_date = movie_date_p.search(dd).group(1)
        # 评分
        movie_score_p = re.compile(r'<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i><',re.S)
        movie_score = movie_score_p.search(dd).group(1) + movie_score_p.search(dd).group(2)
        # 详情页链接
        movie_link_p = re.compile(r'<a href="(.*?)" title="',re.S)
        movie_link = 'https://maoyan.com'+movie_link_p.search(dd).group(1)
        item = {}
        item['movie_title'] = movie_title
        item['movie_actor'] = movie_actor
        item['movie_date'] = movie_date
        item['movie_score'] = movie_score
        item['movie_link'] = movie_link
        # 将数据写入json文件
        print(item)
        movie_list.append(item)


def write_to_json(movie_list):
    #json.load(fp) 从json文件中读出数据，返回一个list或者dict
    #json.dump(list/dict,fp) 将list或者dict 写入json文件中
    with open('maoyan_movie.json','w',encoding='utf-8') as fp:
        json.dump(movie_list,fp)
    print('写入成功')


def main():
    # 确定url
    base_url = 'https://maoyan.com/board/4?offset=%s'
    # 获取每一页的内容
    for i in range(10):
        html_str = get_content(base_url % (i * 10))
        parse_html(html_str)
    # 写入json文件
    write_to_json(movie_list)


if __name__ == '__main__':
    movie_list = []
    main()
