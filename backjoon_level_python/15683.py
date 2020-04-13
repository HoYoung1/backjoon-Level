# https://www.acmicpc.net/problem/15683
# 141156KB	1428ms
# pypy3

from enum import Enum
from copy import deepcopy
import sys

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

minimum_blind_spot = sys.maxsize


class LandType(Enum):
    EMPTY = 0
    WALL = 6
    DETECTED = '#'


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def get_blind_spot_count(matrix):
    result = 0
    for row in matrix:
        for r in row:
            if r == LandType.EMPTY.value:
                result += 1
    return result


def dfs(depth, current_matrix):
    global minimum_blind_spot

    if depth == len(cctvs):
        current_blind_spot = get_blind_spot_count(current_matrix)
        minimum_blind_spot = min(minimum_blind_spot, current_blind_spot)
        return

    x, y = cctvs[depth]
    if matrix[x][y] == 1:
        next_matrix = check_detection(current_matrix, depth, Direction.UP.value, True)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.DOWN.value, True)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.LEFT.value, True)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.RIGHT.value, True)
        dfs(depth + 1, next_matrix)

    elif matrix[x][y] == 2:
        next_matrix = check_detection(current_matrix, depth, Direction.UP.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.DOWN.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.LEFT.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.RIGHT.value, False)
        dfs(depth + 1, next_matrix)
    elif matrix[x][y] == 3:
        next_matrix = check_detection(current_matrix, depth, Direction.UP.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.RIGHT.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.RIGHT.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.DOWN.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.DOWN.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.LEFT.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.LEFT.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.UP.value, False)
        dfs(depth + 1, next_matrix)
    elif matrix[x][y] == 4:
        next_matrix = check_detection(current_matrix, depth, Direction.LEFT.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.UP.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.RIGHT.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.UP.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.RIGHT.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.DOWN.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.RIGHT.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.DOWN.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.LEFT.value, False)
        dfs(depth + 1, next_matrix)

        next_matrix = check_detection(current_matrix, depth, Direction.DOWN.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.LEFT.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.UP.value, False)
        dfs(depth + 1, next_matrix)
    elif matrix[x][y] == 5:
        next_matrix = check_detection(current_matrix, depth, Direction.UP.value, True)
        next_matrix = check_detection(next_matrix, depth, Direction.LEFT.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.RIGHT.value, False)
        next_matrix = check_detection(next_matrix, depth, Direction.DOWN.value, False)
        dfs(depth + 1, next_matrix)


def check_detection(current_matrix, depth, i, should_copy):
    if should_copy:
        next_matrix = deepcopy(current_matrix)
    else:
        next_matrix = current_matrix

    # '#' 표시
    next_x, next_y = cctvs[depth]
    while True:
        next_x = next_x + dx[i]
        next_y = next_y + dy[i]
        if (0 <= next_x < N) is False or (0 <= next_y < M) is False or current_matrix[next_x][
            next_y] == LandType.WALL.value:
            break
        if current_matrix[next_x][next_y] == LandType.EMPTY.value:
            next_matrix[next_x][next_y] = LandType.DETECTED.value
    return next_matrix


def solve(N, M, matrix):
    dfs(0, matrix)

    return minimum_blind_spot


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cctvs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 1 <= matrix[i][j] <= 5:
                cctvs.append((i, j))

    print(solve(N, M, matrix))