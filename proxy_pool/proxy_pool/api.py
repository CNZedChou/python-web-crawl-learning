# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  api.py
@Description    :  use flask to implement the api
@CreateTime     :  2020-7-6 09:48
------------------------------------
@ModifyTime     :  
"""
from flask import Flask,g
from proxy_pool.proxy_pool.db import Redis_Client

__all__=['app']
app = Flask(__name__)
def get_conn():
    if not hasattr(g,'redis_client'):
        g.redis_client = Redis_Client
    return g.redis_client


@app.route('/')
def index():
    return '<h1>欢迎进入代理池系统</h1>'


@app.route('/get')
def get():
    return get_conn().pop()


@app.route('/count')
def count():
    return str(get_conn().queue_len)