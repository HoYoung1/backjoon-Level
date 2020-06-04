# https://www.acmicpc.net/problem/2210

# 리스트로 하지말고 스트링으로 했으면 결과가 더 좋을듯
# 상,하,좌,우

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 29380KB 1012ms
def solve1(matrix):
    from copy import deepcopy
    def dfs(depth, x, y, current_numbers):
        if depth == TARGET_LENGTH - 1:
            answer_numbers.add(current_numbers)
            return

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < MATRIX_SIZE and 0 <= next_y < MATRIX_SIZE:
                dfs(depth + 1, next_x, next_y, current_numbers+str(matrix[next_x][next_y]))

    answer_numbers = set()
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            dfs(0, i, j, str(matrix[i][j]))
    return len(answer_numbers)


# 31980KB 1016ms
def solve2(matrix):
    from collections import deque

    def bfs(i, j):
        dq.append((str(matrix[i][j]), i, j))
        while dq:
            current_numbers, x, y = dq.popleft()
            if len(current_numbers) == TARGET_LENGTH:
                answer_numbers.add(current_numbers)
            else:
                for i in range(4):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    if 0 <= next_x < MATRIX_SIZE and 0 <= next_y < MATRIX_SIZE:
                        dq.append((current_numbers + str(matrix[next_x][next_y]), next_x, next_y))

    answer_numbers = set()
    dq = deque()

    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            bfs(i, j)
    return len(answer_numbers)


if __name__ == '__main__':
    MATRIX_SIZE = 5
    TARGET_LENGTH = 6

    matrix = [list(map(int, input().split())) for _ in range(MATRIX_SIZE)]
    print(solve2(matrix))
