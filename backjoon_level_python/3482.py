from collections import deque

# 위 아래 왼 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(R, C, matrix):
    # 시작점 아무거나 잡기
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '.':
                start_x = i
                start_y = j

    # bfs
    _, nx, ny = bfs(C, R, matrix, start_x, start_y)
    answer, _, _ = bfs(C, R, matrix, nx, ny)
    return answer


def bfs(C, R, matrix, start_x, start_y):
    max_depth = -1
    max_x = None
    max_y = None

    dq = deque()
    visited = [[False] * C for _ in range(R)]
    visited[start_x][start_y] = False
    dq.append((start_x, start_y, 0))
    while dq:
        x, y, depth = dq.popleft()
        if depth > max_depth:
            max_depth = depth
            max_x = x
            max_y = y
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < R and 0 <= next_y < C and visited[next_x][next_y] is False and matrix[next_x][
                next_y] == '.':
                visited[next_x][next_y] = True
                dq.append((next_x, next_y, depth + 1))
    return max_depth, max_x, max_y


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        C, R = map(int, input().split())
        matrix = [input() for _ in range(R)]

        print('Maximum rope length is {}.'.format(solve(R, C, matrix)))
