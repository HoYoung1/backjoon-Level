import heapq
import sys
from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시간초과 bfs
def solve(N, M, matrix):
    result = sys.maxsize

    dq = deque()
    dq.append((0, 0, 0))
    while dq:
        r, c, broken_wall_count = dq.popleft()
        if r == N - 1 and c == M - 1:
            result = min(broken_wall_count, result)
            continue

        if r + 1 < N:
            next_broken_wall_count = broken_wall_count + int(matrix[r + 1][c])
            dq.append((r + 1, c, next_broken_wall_count))

        if c + 1 < M:
            next_broken_wall_count = broken_wall_count + int(matrix[r][c + 1])
            dq.append((r, c + 1, next_broken_wall_count))
    return result


def solve2(N, M, matrix):
    q = []
    visited = [[False] * M for _ in range(N)]

    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = True
    while q:
        broken_wall_count, x, y = heapq.heappop(q)
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x == N-1 and next_y == M-1:
                return broken_wall_count
            if 0<=next_x<N and 0<=next_y<M and visited[next_x][next_y] is False:
                next_broken_wall_count = broken_wall_count + int(matrix[next_x][next_y])
                heapq.heappush(q, (next_broken_wall_count, next_x, next_y))
                visited[next_x][next_y] = True
    return 0


if __name__ == '__main__':
    M, N = map(int, input().split())
    matrix = [input() for _ in range(N)]
    print(solve2(N, M, matrix))
