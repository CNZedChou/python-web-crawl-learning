import numpy as np
# 使用邻接矩阵表示图的拓扑排序
def topological_sort(g):
    n = len(g)
    # 获取所有入度为0的结点
    q = []
    for j in range(n):
        flag = True
        for i in range(n):
            if g[i][j] == 1:
                flag = False
                break
        if flag:
            q.insert(0, j)

    li = []  # 记录结果
    while len(q) > 0:
        # p出队，把从p出度的数据置为0
        p = q.pop()
        li.append(p)
        for i in range(n):
            if g[p][i] == 1:
                g[p][i] = 0  # 去掉连通
                # 如果结点i的入度为0则入队结点i
                in_degree_count = 0
                for u in g:
                    if u[i] == 1:
                        in_degree_count += 1
                if in_degree_count == 0:
                    q.insert(0, i)

    return li


if __name__ == '__main__':
    # 用邻接矩阵表示图
    # 初始化图的数据，连通的标记为1
    g = np.zeros(shape=(13, 13), dtype='int')
    # g[i][j] = 1 表示 i -> j
    g[0][1] = g[0][5] = g[0][6] = 1
    g[2][0] = g[2][3] = 1
    g[3][5] = 1
    g[5][4] = 1
    g[6][4] = g[6][9] = 1
    g[7][6] = 1
    g[8][7] = 1
    g[9][10] = g[9][11] = g[9][12] = 1
    g[11][12] = 1

    result = topological_sort(g)
    print(result);