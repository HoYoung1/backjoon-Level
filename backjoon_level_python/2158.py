import heapq
import sys
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(V, R, C, matrix):
    hq = []
    time_matrix = [[sys.maxsize] * C for _ in range(R)]

    time_matrix[0][0] = 0
    heapq.heappush(hq, (0, V, 0, 0))
    while hq:
        current_time, current_v, x, y = heapq.heappop(hq)
        if x == R - 1 and y == C - 1:
            break
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < R and 0 <= next_y < C:
                next_v = current_v * 2 ** (matrix[x][y] - matrix[next_x][next_y])
                next_time = current_time + 1 / current_v
                if next_time < time_matrix[next_x][next_y]:
                    time_matrix[next_x][next_y] = next_time
                    heapq.heappush(hq, (next_time, next_v, next_x, next_y))
    return current_time


if __name__ == '__main__':
    V, R, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(R)]
    print('{:.2f}'.format(solve(V, R, C, matrix)))
