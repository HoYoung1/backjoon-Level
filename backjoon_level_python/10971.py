# TODO : 다른 문제 풀이 꼭 확인하기

import sys


def dfs(depth, current_cost, current_city, start_city):
    global min_travel_cost

    if depth == N:
        if matrix[current_city][start_city] != 0:  # 시작점으로 갈 수 있는가?
            min_travel_cost = min(min_travel_cost, current_cost + matrix[current_city][start_city])
    else:
        for i in range(N):
            if matrix[current_city][i] != 0 and visited[i] is False:
                visited[i] = True
                dfs(depth+1, current_cost+matrix[current_city][i], i, start_city)
                visited[i] = False


#118352KB	1048ms  O(N!)
def solve():
    for i in range(N):
        visited[i] = True
        dfs(1, 0, i, i)
        visited[i] = False
    return min_travel_cost


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]

    min_travel_cost = sys.maxsize
    print(solve())