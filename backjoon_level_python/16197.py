from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(N, M, matrix):
    answer = None
    coin_1, coin_2 = get_coin_locations(M, N, matrix)

    # visited[N][M][N][M]
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append((coin_1[0], coin_1[1], coin_2[0], coin_2[1], 0))
    visited[coin_1[0]][coin_1[1]][coin_2[0]][coin_2[1]] = True

    answer = bfs(M, N, dq, visited)
    return answer


def bfs(M, N, dq, visited):
    while dq:
        x1, y1, x2, y2, depth = dq.popleft()
        if depth == 10:
            return -1
        # 왼 오 위 아래
        for i in range(4):
            coin_1_out_flag = False
            coin_2_out_flag = False
            next_x1 = x1 + dx[i]
            next_y1 = y1 + dy[i]
            if not (0 <= next_x1 < N) or not (0 <= next_y1 < M):
                coin_1_out_flag = True
            elif matrix[next_x1][next_y1] == '#':
                next_x1 = x1
                next_y1 = y1

            next_x2 = x2 + dx[i]
            next_y2 = y2 + dy[i]
            if not (0 <= next_x2 < N) or not (0 <= next_y2 < M):
                coin_2_out_flag = True
            elif matrix[next_x2][next_y2] == '#':
                next_x2 = x2
                next_y2 = y2

            if coin_1_out_flag & coin_2_out_flag:
                continue
            elif coin_1_out_flag ^ coin_2_out_flag:
                return depth + 1
            elif visited[next_x1][next_y1][next_x2][next_y2]:
                continue
            elif next_x1 == next_x2 and next_y1 == next_y2:
                continue
            else:
                visited[next_x1][next_y1][next_x2][next_y2] = True
                dq.append((next_x1,next_y1,next_x2,next_y2, depth+1))

    return -1


def get_coin_locations(M, N, matrix):
    coin_1 = None
    coin_2 = None
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'o':
                if coin_1 is None:
                    coin_1 = (i, j)
                else:
                    coin_2 = (i, j)
    return coin_1, coin_2


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [input() for i in range(N)]
    print(solve(N, M, matrix))
