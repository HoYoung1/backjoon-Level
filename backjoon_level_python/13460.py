# https://www.acmicpc.net/problem/13460

# 32156KB 2860ms
# 접근방법이 잘못됨. 시간초과 아슬아슬 했을듯
# 시간이 훨씬 짧은 코드도 많은데 다음엔 dfs를 쓰지말고 풀어볼 것

import sys
from enum import Enum
from collections import deque


class LandType(Enum):
    WALL = '#'
    BLUE = 'B'
    RED = 'R'
    EMPTY = '.'
    HOLE = 'O'


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


minimum_count = sys.maxsize

# 상, 하, 좌, 우
dy = [0, 0, -1, 1]

dx = [-1, 1, 0, 0]
dq = deque()


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def dfs(depth, direction, current_red_loc, current_blue_loc):
    global minimum_count

    if depth > MAXIMUM_MOVE:
        # 10번 이하로 움직여야함
        return

    hole_found_red = False
    hole_found_blue = False

    # move red
    dq.clear()
    dq.append(current_red_loc)
    while dq:
        x, y = dq.popleft()
        next_red_loc = [x, y]

        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if matrix[next_x][next_y] == LandType.HOLE.value:
            hole_found_red = True
            break
        elif matrix[next_x][next_y] != LandType.WALL.value:
            dq.append([next_x, next_y])

    # move blue
    dq.clear()
    dq.append(current_blue_loc)
    while dq:
        x, y = dq.popleft()
        next_blue_loc = [x, y]

        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if matrix[next_x][next_y] == LandType.HOLE.value:
            hole_found_blue = True
            break
        elif matrix[next_x][next_y] != LandType.WALL.value:
            dq.append([next_x, next_y])

    if hole_found_blue is True:
        return
    elif hole_found_red is True:
        minimum_count = min(minimum_count, depth)
        return

    # didnt move
    if next_red_loc == current_red_loc and next_blue_loc == current_blue_loc:
        return

    # 겹쳤을 경우 위치보정
    if next_red_loc == next_blue_loc:
        if direction == Direction.UP.value:
            if current_red_loc[0] > current_blue_loc[0]:
                next_red_loc[0] += 1
            else:
                next_blue_loc[0] += 1
        elif direction == Direction.DOWN.value:
            if current_red_loc[0] > current_blue_loc[0]:
                next_blue_loc[0] -= 1
            else:
                next_red_loc[0] -= 1
        elif direction == Direction.LEFT.value:
            if current_red_loc[1] > current_blue_loc[1]:
                next_red_loc[1] += 1
            else:
                next_blue_loc[1] += 1
        elif direction == Direction.RIGHT.value:
            if current_red_loc[1] > current_blue_loc[1]:
                next_blue_loc[1] -= 1
            else:
                next_red_loc[1] -= 1

    # for debug

    # cr_x, cr_y = current_red_loc
    # cb_x, cb_y = current_blue_loc
    # matrix[cr_x][cr_y] = LandType.EMPTY.value
    # matrix[cb_x][cb_y] = LandType.EMPTY.value
    #
    # nr_x, nr_y = next_red_loc
    # nb_x, nb_y = next_blue_loc
    # matrix[nr_x][nr_y] = LandType.RED.value
    # matrix[nb_x][nb_y] = LandType.BLUE.value

    # print_matrix(matrix)

    for d in range(4):
        dfs(depth + 1, d, next_red_loc, next_blue_loc)


def solve(N, M, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == LandType.BLUE.value:
                blue_loc = [i, j]
            elif matrix[i][j] == LandType.RED.value:
                red_loc = [i, j]

    for d in range(4):
        dfs(1, d, red_loc, blue_loc)

    if minimum_count == sys.maxsize:
        return -1
    else:
        return minimum_count

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    MAXIMUM_MOVE = 10
    print(solve(N, M, matrix))
