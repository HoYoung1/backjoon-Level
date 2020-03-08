from enum import Enum
from collections import deque

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


class CaveStatus(Enum):
    EMPTY = '.'
    MINERAL = 'x'


def print_map(map):
    for row in map:
        for i in row:
            print(i, end="")
        print()


def check_cluster(init_x, init_y):
    """
    :return cluster_is_from_land, cluster
    """
    visited = [[False for _ in range(C)] for _ in range(R)]
    cluster = []

    # BFS
    dq = deque()
    dq.append((init_x, init_y))
    visited[init_x][init_y] = True
    cluster.append((init_x, init_y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C:
                if visited[x+dx[i]][y+dy[i]] or \
                        matrix[x + dx[i]][y + dy[i]] == CaveStatus.EMPTY.value:
                    continue
                else:
                    dq.append((x+dx[i], y+dy[i]))
                    visited[x+dx[i]][y+dy[i]] = True
                    cluster.append((x+dx[i], y+dy[i]))

                    if x + dx[i] == R-1:  # 땅에 붙어있는 클러스터인가?
                        # print_map(visited)
                        return True, cluster
    # print_map(visited)
    return False, cluster


def down_cluster(cluster):
    loop = True
    while loop:
        for x, y in cluster:
            matrix[x][y] = CaveStatus.EMPTY.value
        for x, y in cluster:
            if x+1 == R or matrix[x+1][y] == CaveStatus.MINERAL.value:
                loop = False
                break

        if loop:
            for idx, (x, y) in enumerate(cluster):
                cluster[idx] = (x+1, y)
        for x, y in cluster:
            matrix[x][y] = CaveStatus.MINERAL.value


def break_mineral(row_idx, col_idx):
    matrix[row_idx][col_idx] = CaveStatus.EMPTY.value

    for i in range(4):
        if 0 <= row_idx+dx[i] < R and 0 <= col_idx+dy[i] < C and \
                matrix[row_idx+dx[i]][col_idx+dy[i]] == CaveStatus.MINERAL.value:
            is_from_land, cluster = \
                check_cluster(row_idx + dx[i], col_idx + dy[i])

            if not is_from_land:
                # 땅으로 부터 붙어있는 클러스터가 아니라면
                # print_map(matrix)
                down_cluster(cluster)
                # print_map(matrix)


def solve():
    for idx, height in enumerate(heights):
        # 맨 아래가 1 , 맨 위가 R 이므로 치환
        row_idx = R - height

        for i in range(0, C):
            # 홀 수 인 경우 오른쪽부터
            if idx % 2 != 0:
                i = C - 1 - i

            if matrix[row_idx][i] == CaveStatus.MINERAL.value:
                break_mineral(row_idx, i)
                break


if __name__ == '__main__':
    # 동굴의 크기 R과 C가 주어진다. (1 ≤ R,C ≤ 100)
    R, C = map(int, input().split())

    matrix = [list(input()) for _ in range(R)]
    # . 으로 하니까 잘 안보임 o 로 변경해서 디버깅 편하게
    # for row in matrix:
    #     for idx, x in enumerate(row):
    #         if x == '.':
    #             row[idx] = 'o'

    # print_map(matrix)
    # 막대를 던진 횟수 N
    N = int(input())

    # 막대를 던진 높이
    heights = list(map(int, input().split()))

    solve()
    print_map(matrix)
