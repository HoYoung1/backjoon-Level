# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
from copy import deepcopy
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def print_matrix():
    for row in matrix:
        print(row)
    print()


def draw_curve(x, y, d, g):
    stack = []

    matrix[x][y] = g # 시작점 마킹

    current_x = x + dx[d]
    current_y = y + dy[d]
    matrix[current_x][current_y] = g  # 시작점에서 연결된 부분도 마킹
    stack.append(d)

    for _ in range(g):
        for last_d in deepcopy(list(reversed(stack))):
            d = (last_d+1) % 4
            stack.append(d)
            current_x = current_x + dx[d]
            current_y = current_y + dy[d]
            matrix[current_x][current_y] = g
        # print_matrix()


def get_rectangle_count(matrix):
    count = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] > -1 and matrix[i+1][j] > -1 and matrix[i][j+1] > -1 and matrix[i+1][j+1] > -1:
                count += 1
    return count


if __name__ == '__main__':
    N = int(input())  # 드래곤 커브의 갯수, 1<=N<=20
    MATRIX_SIZE = 101
    matrix = [[-1]*MATRIX_SIZE for _ in range(MATRIX_SIZE)]  # init map
    for _ in range(N):
        x, y, d, g = map(int, input().split())  # 0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10
        draw_curve(y, x, d, g)
    print(get_rectangle_count(matrix))
    # print_matrix()



