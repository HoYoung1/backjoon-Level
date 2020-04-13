# https://www.acmicpc.net/problem/14502
# 133180KB 952ms
# pypy3


from enum import Enum
from collections import deque
from copy import deepcopy

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
max_empty_count = 0


class LandType(Enum):
    EMPTY = 0
    WALL = 1
    VIRUS = 2
    MY_WALL = 3


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def dfs(depth, start_i, start_j):
    global max_empty_count

    if depth == 3:
        # print_matrix(matrix)
        # print()
        temp_matrix_for_bfs = bfs(deepcopy(matrix), deepcopy(virus_locations))

        # print_matrix(temp_matrix_for_bfs)
        # print()

        empty_count = get_empty_count(temp_matrix_for_bfs)

        max_empty_count = max(max_empty_count, empty_count)
        return

    for i in range(start_i, len(matrix)):
        for j in range(start_j, len(matrix[i])):
            start_j = 0
            if not visited[i][j] and matrix[i][j] == LandType.EMPTY.value:
                visited[i][j] = True
                matrix[i][j] = LandType.MY_WALL.value
                dfs(depth+1, i, j)
                matrix[i][j] = LandType.EMPTY.value
                visited[i][j] = False


def get_empty_count(temp_matrix_for_bfs):
    empty_count = 0
    for i in range(len(temp_matrix_for_bfs)):
        for j in range(len(temp_matrix_for_bfs[i])):
            if temp_matrix_for_bfs[i][j] == LandType.EMPTY.value:
                empty_count += 1
    return empty_count


def bfs(temp_matrix_for_bfs, virus_locations):
    while len(virus_locations) != 0:
        poped_x, poped_y = virus_locations.popleft()
        for d in range(4):
            check_x = dx[d] + poped_x
            check_y = dy[d] + poped_y
            if 0 <= check_x < N and 0 <= check_y < M and temp_matrix_for_bfs[check_x][check_y] == LandType.EMPTY.value:
                temp_matrix_for_bfs[check_x][check_y] = LandType.VIRUS.value
                virus_locations.append((check_x, check_y))

    # print_matrix(temp_matrix_for_bfs)
    return temp_matrix_for_bfs


def solve():
    dfs(0, 0, 0)
    return max_empty_count


if __name__ == '__main__':
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    virus_locations = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == LandType.VIRUS.value:
                virus_locations.append((i, j))

    visited = [[False] * M for _ in range(N)]

    # print_matrix(visited)

    max_empty_count = solve()
    print(max_empty_count)
