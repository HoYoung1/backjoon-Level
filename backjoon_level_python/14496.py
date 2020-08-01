import sys
from collections import deque

answer = sys.maxsize

input = sys.stdin.readline


# dfs로는 안됨 ㅠ.ㅠ
def solve(N, M, matrix):
    global answer

    min_distance = [sys.maxsize] * (N+1)

    def dfs(depth, current_v):
        global answer

        if current_v == b:
            answer = min(answer, depth)
            return
        if depth >= answer:
            return

        for i in range(1, N+1):
            if matrix[current_v][i] == 1 and visited[i] is False and min_distance[i] > depth:
                min_distance[i] = depth

                visited[i] = True
                dfs(depth+1, i)
                visited[i] = False
    dfs(0, a)

    if answer == sys.maxsize:
        answer = -1
    return answer


def solve2(N, M, matrix):
    answer = -1

    visited = [False] * (N+1)

    dq = deque()
    dq.append((a, 0))
    visited[a] = True

    while dq:
        u, depth = dq.popleft()
        for v in range(1, N+1):
            if matrix[u][v] is True and visited[v] is False:
                if v == b:
                    answer = depth + 1
                    break
                dq.append((v, depth + 1))
                visited[v] = True
        if answer != -1:
            break
    return answer


11


if __name__ == '__main__':
    a, b = map(int, input().split())
    N, M = map(int, input().split())
    matrix = [[False]*(N+1) for _ in range(N+1)]
    visited = [False]*(N+1)
    for i in range(M):
        u, v = map(int, input().split())
        matrix[u][v] = True
        matrix[v][u] = True
        
    if a == b:
        print(0)
    else:
        print(solve2(N, M, matrix))
