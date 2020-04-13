29284KB	580ms

def print_matrix(visited):
    for row in visited:
        print(row)
    print()


def calculate_horizon():
    total_sum = 0

    for i in range(N):
        row_sum = 0
        for j in range(M):
            if is_horizon[i][j] is True:
                row_sum = row_sum * 10 + matrix[i][j]
            else:
                total_sum += row_sum
                row_sum = 0
        total_sum += row_sum
    return total_sum


def calculate_vertical():
    total_sum = 0
    for j in range(M):
        col_sum = 0
        for i in range(N):
            if is_horizon[i][j] is False:
                col_sum = col_sum * 10 + matrix[i][j]
            else:
                total_sum += col_sum
                col_sum = 0
        total_sum += col_sum
    return total_sum


def dfs(x, y):
    """
    행렬의 모든 원소가 한번은 True, 한번은 False 가지도록 완전 탐색
    """
    global max_value

    if x == N:
        # print_matrix(visited)]
        h = calculate_horizon()
        v = calculate_vertical()
        max_value = max(max_value, h + v)
        return
    if y == M:
        dfs(x + 1, 0)
        return
    is_horizon[x][y] = True
    dfs(x, y + 1)
    is_horizon[x][y] = False
    dfs(x, y + 1)


def solve():
    dfs(0, 0)
    return max_value


if __name__ == '__main__':
    N, M = map(int, input().split())

    matrix = [list(map(int, list(input()))) for _ in range(N)]
    is_horizon = [[False] * M for _ in range(N)]

    max_value = 0

    print(solve())
