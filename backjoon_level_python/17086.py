# 질문
# https://www.acmicpc.net/source/20095410
# 이사람은 왜 속도차이가많이날까,,
from collections import deque

# 상 하 좌 우 상좌 상우 하좌 하우
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def solve(N, M, matrix):
    answer = 0

    shark_locations = get_shark_xy(M, N, matrix)


    while shark_locations:
        x, y = shark_locations.popleft()

        dq = deque()
        visited = [[False] * M for _ in range(N)]

        dq.append((0, x, y))
        visited[x][y] = True
        matrix[x][y] = 0

        while dq:
            distance, s_x, s_y = dq.popleft()
            for i in range(8):
                next_x = s_x + dx[i]
                next_y = s_y + dy[i]
                if 0 <= next_x < N and 0 <= next_y < M and visited[next_x][next_y] is False and matrix[next_x][next_y] > distance:
                    visited[next_x][next_y] = True
                    matrix[next_x][next_y] = distance + 1
                    dq.append((distance + 1, next_x, next_y))
        # print_matrix(matrix)
    for row in matrix:
        answer = max(answer, max(row))
    return answer

def get_shark_xy(M, N, matrix):
    dq = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dq.append((i, j))
            matrix[i][j] = 9999
    return dq


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(solve(N, M, matrix))
