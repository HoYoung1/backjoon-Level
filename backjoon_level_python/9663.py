from enum import Enum


class LandStatus(Enum):
    CLEAN = 0
    QUEEN = 1
    RANGE = 2


def mark_land_status(x, y, value):
    """
    3방향만 표시하면 됨 (5, 6, 7시 방향)
    """
    # 아래로
    for i in range(x+1, N):
        matrix[i][y] += value
    # 왼쪽 아래
    i = 1
    while 0 <= x+i < N and 0 <= y-i < N:
        matrix[x + i][y - i] += value
        i += 1
    # 오른쪽 아래
    i = 1
    while 0 <= x + i < N and 0 <= y + i < N:
        matrix[x + i][y + i] += value
        i += 1


def print_matrix():
    for row in matrix:
        print(row)
    print()


def dfs(depth):
    global count

    if depth == N:
        # print_matrix()
        count += 1
        return

    row = depth
    for col in range(0, N):
        if matrix[row][col] == LandStatus.CLEAN.value:
            mark_land_status(row, col, LandStatus.RANGE.value)
            matrix[row][col] = LandStatus.QUEEN.value  # just for debug
            dfs(depth + 1)
            matrix[row][col] = LandStatus.CLEAN.value  # just for debug
            mark_land_status(row, col, LandStatus.RANGE.value * -1)


def solution(N):
    depth = 0
    dfs(depth)
    return count


if __name__ == '__main__':
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    print(solution(N))
