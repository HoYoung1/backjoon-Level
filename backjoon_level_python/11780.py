import sys
from copy import deepcopy


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


# def solve(n, m, city_infos):
#     path = [[[] for _ in range(n+1)] for _ in range(n+1)]
#
#     bus_info = [[sys.maxsize]*(n+1) for _ in range(n+1)]
#     for city_info in city_infos:
#         start_city_num, end_city_num, cost = city_info
#         if bus_info[start_city_num][end_city_num] > cost:
#             bus_info[start_city_num][end_city_num] = cost
#             path[start_city_num][end_city_num].append(start_city_num)
#             path[start_city_num][end_city_num].append(end_city_num)
#
#     dp = deepcopy(bus_info)
#
#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 if i == j:
#                     dp[i][j] = 0
#                     # path[i] = []
#                 else:
#                     if dp[i][j] > dp[i][k] + dp[k][j]:
#                         dp[i][j] = dp[i][k] + dp[k][j]
#                         path[i][j] = path[i][k][:-1] + [k] + path[k][j][1:]
#
#     # answer
#     for i in range(1,n+1):
#         for j in range(1, n+1):
#             if dp[i][j] == sys.maxsize:
#                 print('0', end=" ")
#             else:
#                 print(dp[i][j], end=" ")
#         print()
#
#     for i in range(1,n+1):
#         for j in range(1, n+1):
#             print(len(path[i][j]), end=" ")
#             for k in path[i][j]:
#                 print(k, end=" ")
#             print()


def solve(n, m, city_infos):
    next = [[-1]*(n+1) for _ in range(n+1)]
    dist = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    for city_info in city_infos:
        u, v, cost = city_info
        if dist[u][v] > cost:
            dist[u][v] = cost
            next[u][v] = u


    dp = deepcopy(dist)

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    dp[i][j] = 0
                elif dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[k][j]

    # answer
    for i in range(1,n+1):
        for j in range(1, n+1):
            if dp[i][j] == sys.maxsize:
                print('0', end=" ")
            else:
                print(dp[i][j], end=" ")
        print()

    for i in range(1,n+1):
        for j in range(1, n+1):
            if next[i][j] == -1:
                print('0')
            else:
                path = []
                pre = j
                path.append(pre)
                while i != next[i][pre]:
                    pre = next[i][pre]
                    path.insert(0,pre)
                print(len(path)+1,end=" ")
                print(i,end = " ")
                print(' '.join(list(map(str, path))))




if __name__ == '__main__':
    n = int(input())
    m = int(input())

    l = []
    for _ in range(m):
        start_city_num, end_city_num, cost = map(int, input().split())  # 1 <= cost <= 100000
        l.append((start_city_num, end_city_num, cost))

    solve(n, m, l)


