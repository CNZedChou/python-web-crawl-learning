# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  table.py
@Description    :  
@CreateTime     :  2019-12-28 15:47
------------------------------------
@ModifyTime     :  
"""
def topological_sort2(g):
    n = len(g)
    # 计算所有结点的入度
    in_degree = [0] * n
    for i in range(n):
        for k in g[i]:
            in_degree[k] += 1
    # 入度为0的结点
    in_degree_0 = []
    for i in range(n):
        if in_degree[i] == 0:
            in_degree_0.insert(0, i)

    li = []  # 记录结果
    while len(in_degree_0) > 0:
        # p出队
        p = in_degree_0.pop()
        li.append(p)
        for k in g[p]:
            # 对应结点的入度减1
            in_degree[k] -= 1
            if in_degree[k] == 0:
                in_degree_0.insert(0, k)

    return li


if __name__ == '__main__':
    # 用邻接表表示图
    g2 = [[]] * 13
    g2[0] = [1, 5, 6]
    g2[2] = [3]
    g2[3] = [5]
    g2[5] = [4]
    g2[6] = [4, 9]
    g2[7] = [6]
    g2[8] = [7]
    g2[9] = [10, 11, 12]
    g2[11] = [12]
    result2 = topological_sort2(g2)
    print(result2)
