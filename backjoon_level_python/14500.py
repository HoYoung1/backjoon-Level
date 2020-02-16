dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def debugging():
    for row in visited:
        print(row)
    print()


def dfs(depth, i, j, stack_sum):
    global maximum_sum

    # debugging()
    if depth == 3:
        maximum_sum = max(maximum_sum, stack_sum)
        return
    else:
        for idx in range(4):
            temp_x = i + dx[idx]
            temp_y = j + dy[idx]
            if is_available_index(temp_x, temp_y) and visited[temp_x][temp_y] is False:
                visited[temp_x][temp_y] = True
                dfs(depth + 1, temp_x, temp_y, stack_sum + matrix[temp_x][temp_y])
                visited[temp_x][temp_y] = False


def is_available_index(i, j):
    return 0 <= i < N and 0 <= j < M


def check_fuck_shape():
    global maximum_sum

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            try:
                # ㅜ
                maximum_sum = max(maximum_sum,
                                  matrix[i][j] + matrix[i - 1][j] + matrix[i - 1][j - 1] + matrix[i - 1][j + 1])
            except IndexError:
                pass
            try:
                # ㅗ
                maximum_sum = max(maximum_sum,
                                  matrix[i][j] + matrix[i + 1][j] + matrix[i + 1][j - 1] + matrix[i + 1][j + 1])
            except IndexError:
                pass
            try:
                # ㅏ
                maximum_sum = max(maximum_sum,
                                  matrix[i][j] + matrix[i][j - 1] + matrix[i - 1][j - 1] + matrix[i + 1][j - 1])
            except IndexError:
                pass
            try:
                # ㅓ
                maximum_sum = max(maximum_sum,
                                  matrix[i][j] + matrix[i][j + 1] + matrix[i - 1][j + 1] + matrix[i + 1][j + 1])
            except IndexError:
                pass


def solution():
    depth = 0
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            if i == 3 and j == 7:
                pass
            visited[i][j] = True
            dfs(depth, i, j, matrix[i][j])
            visited[i][j] = False

    check_fuck_shape()
    return maximum_sum


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # initialize
    visited = [[False] * M for _ in range(N)]
    maximum_sum = 0

    print(solution())
