import sys
from enum import Enum
from collections import deque
input = sys.stdin.readline


class MatrixValue(Enum):
    EMPTY = '.'
    WALL = '#'
    RABBIT = 'R'
    CARROT = 'C'
    DOOR = 'O'


def get_R_location(N, M, matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == MatrixValue.RABBIT.value:
                return i, j


def solve(N, M, matrix):
    answer = -1
    dp = [[-1] * M for _ in range(N)]

    x, y = get_R_location(N, M, matrix)

    dq = deque()
    dq.append((x, y, 0))
    while dq:
        current_x, current_y, current_carrot = dq.popleft()

        dx = [-1, 0, 1]
        dy = [1, 1, 1]

        for i in range(3):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and matrix[next_x][next_y] != MatrixValue.WALL.value:
                next_carrot_num = dp[next_x][next_y]+1 if dp[next_x]

                if next_carrot_num <= current_carrot
                dq.append((next_x, next_y, dp[current_x][current_y]))

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    print(solve(N, M, matrix))
    # assert solve(3,5,[list("RC#OO"),list(".#CCC"),list("..O..")]) == 3
