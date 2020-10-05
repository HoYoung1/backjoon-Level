import heapq
import sys

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solve(N, M, matrix):
    weight = [[0] * M for _ in range(N)]
    dist = [[1e9] * M for _ in range(N)]
    pq = []

    # init
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'S':
                dist[i][j] = 0
                heapq.heappush(pq, (0,i,j))
            elif matrix[i][j] == 'g':
                weight[i][j] = 5000
                for k in range(4):
                    next_x = i + dx[k]
                    next_y = j + dy[k]
                    if 0 <= next_x < N and 0 <= next_y < M and matrix[next_x][next_y] == '.':
                        weight[next_x][next_y] = 1

    # print_matrix(dist)
    # print_matrix(matrix)

    # dijkstra
    while pq:
        distance, x, y = heapq.heappop(pq)
        if matrix[x][y] == 'F':
            # find Flower
            print(dist[x][y]//5000, dist[x][y]%5000)
            sys.exit(0)

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                next_distnace = distance + weight[next_x][next_y]
                if dist[next_x][next_y] > next_distnace:
                    dist[next_x][next_y] = next_distnace
                    heapq.heappush(pq, (next_distnace, next_x, next_y))

    # print_matrix(dist)
    # print_matrix(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    solve(N, M, matrix)