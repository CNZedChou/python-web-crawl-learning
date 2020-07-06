# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  run.py
@Description    :  
@CreateTime     :  2020-7-1 21:12
------------------------------------
@ModifyTime     :  
"""
from proxy_pool.proxy_pool.scheduler import Scheduler
from proxy_pool.proxy_pool.api import app


def main():
    s = Scheduler()
    s.run()
    app.run()


if __name__ == '__main__':
    main()

