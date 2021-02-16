from collections import deque
from enum import Enum
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class LandType(Enum):
    WALL = '#'
    EMPTY = '.'
    INIT = 'J'
    FIRE = 'F'


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def solve(R, C, matrix):
    def find_target(target):
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == target:
                    return i, j
        return -1, -1

    fire_q = deque()
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == LandType.FIRE.value:
                fire_q.append((i, j))

    i_x, i_y = find_target(LandType.INIT.value)
    jihun_q = deque()
    jihun_q.append((i_x, i_y, 0))
    visited[i_x][i_y] = True


    while True:
        fire_nq = deque()
        for i in range(len(fire_q)):
            x, y = fire_q[i]
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != LandType.WALL.value and matrix[nx][ny] != LandType.FIRE.value:
                    fire_nq.append((nx, ny))
                    matrix[nx][ny] = LandType.FIRE.value

        # print_matrix(matrix)
        # print()
        # 지훈이 움직일 차례
        jihun_nq = deque()
        for i in range(len(jihun_q)):
            x, y, t = jihun_q[i]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 탈출조건
                if not (0 <= nx < R) or not (0 <= ny < C):
                    return t + 1
                if visited[nx][ny] is False and matrix[nx][ny] != LandType.WALL.value and matrix[nx][ny] != LandType.FIRE.value:
                    jihun_nq.append((nx, ny, t + 1))
                    visited[nx][ny] = True

        fire_q = fire_nq
        jihun_q = jihun_nq

        if not jihun_q:
            break
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    R, C = map(int, input().rstrip().split())
    matrix = [list(input().rstrip()) for _ in range(R)]
    visited = [[False] * C for _ in range(R)]

    print(solve(R, C, matrix))
