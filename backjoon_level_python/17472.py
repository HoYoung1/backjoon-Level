import sys
from enum import Enum
from collections import deque


class LandType(Enum):
    SEA = '0'
    LAND = '1'


# 위,아래,왼,오른
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

land_q = deque()


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def is_connected(graph):
    flag = False
    for d in graph:
        if d:
            flag = True
    return flag


def count_land_num(matrix):
    land_count = 1  # from 1 to ~

    dq = deque()
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == -1:
                matrix[i][j] = land_count
                visited[i][j] = True
                dq.append((i, j))
                land_q.append((i, j, matrix[i][j], 0, 0))
                land_q.append((i, j, matrix[i][j], 0, 1))
                land_q.append((i, j, matrix[i][j], 0, 2))
                land_q.append((i, j, matrix[i][j], 0, 3))

                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        # 4방향
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < N and 0 <= next_y < M and matrix[next_x][next_y] == -1 \
                                and visited[next_x][next_y] is False:
                            matrix[next_x][next_y] = land_count
                            visited[next_x][next_y] = True
                            dq.append((next_x, next_y))
                            land_q.append((next_x, next_y, matrix[next_x][next_y], 0, 0))
                            land_q.append((next_x, next_y, matrix[next_x][next_y], 0, 1))
                            land_q.append((next_x, next_y, matrix[next_x][next_y], 0, 2))
                            land_q.append((next_x, next_y, matrix[next_x][next_y], 0, 3))

                land_count += 1
    return land_count - 1


def find_bridge(matrix, graph):
    edges = []
    while land_q:
        x, y, land, depth, direction = land_q.popleft()
        # print(x,y,land,depth,direction)
        next_x, next_y = x + dx[direction], y + dy[direction]

        # 이 조건은 안됨.
        if not (0 <= next_x < N) or not (0 <= next_y < M):
            continue
        if matrix[x][y] != 0 and matrix[x][y] == matrix[next_x][next_y]:
            continue

        if matrix[next_x][next_y] == 0:
            land_q.append((next_x, next_y, land, depth + 1, direction))
        else:
            # 육지 도달
            if depth < 2:
                # print('도달할 수 없는 육지 다리길이는 최소 2')
                continue
            else:
                target_land = matrix[next_x][next_y]
                if target_land in graph[land]:
                    graph[land][target_land] = min(graph[land][target_land], depth)
                    graph[target_land][land] = min(graph[target_land][land], depth)
                else:
                    graph[land][target_land] = depth
                    graph[target_land][land] = depth


def minimum_spanning_tree(graph):
    result = 0
    edge_count = 0

    edges = []
    table = list(range(len(graph)))

    for i in range(1, len(graph)):
        for key in graph[i]:
            edges.append((i, key, graph[i][key]))
    edges.sort(key=lambda edge: edge[2])

    def find_parent(x):
        if x == table[x]:
            return x
        return find_parent(table[x])

    for edge in edges:
        a, b, weight = edge
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        if parent_a != parent_b:
            table[parent_a] = parent_b
            result += weight
            edge_count += 1

    if edge_count < len(graph)-2:
        return -1
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                matrix[i][j] = -1

    land_num = count_land_num(matrix)
    # print(land_num)

    graph = [{} for _ in range(land_num + 1)]
    find_bridge(matrix, graph)
    # print_matrix(graph)


    print(minimum_spanning_tree(graph))
