from collections import deque
from enum import Enum

M_dq = deque()
Z_dq = deque()

# 위, 아래, 왼, 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    LEFT = 2
    RIGHT = 3


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def get_starting_point(start_x, start_y):
    next_x = start_x + dx[0]
    next_y = start_y + dy[0]
    if 0 <= next_x < R and 0 <= next_y < C and matrix[start_x + dx[0]][start_y + dy[0]] in ['|', '+', '1', '4']:
        return next_x, next_y, Direction.NORTH.value

    next_x = start_x + dx[1]
    next_y = start_y + dy[1]
    if 0 <= next_x < R and 0 <= next_y < C and matrix[start_x + dx[1]][start_y + dy[1]] in ['|', '+', '2', '3']:
        return next_x, next_y, Direction.SOUTH.value

    next_x = start_x + dx[2]
    next_y = start_y + dy[2]
    if 0 <= next_x < R and 0 <= next_y < C and matrix[start_x + dx[2]][start_y + dy[2]] in ['-', '+', '1', '2']:
        return next_x, next_y, Direction.LEFT.value

    next_x = start_x + dx[3]
    next_y = start_y + dy[3]
    if 0 <= next_x < R and 0 <= next_y < C and matrix[start_x + dx[3]][start_y + dy[3]] in ['-', '+', '3', '4']:
        return next_x, next_y, Direction.RIGHT.value


def get_next_xy(x, y, d):
    if d == 0:
        if matrix[x][y] in ['|', '+']:
            d = 0
        elif matrix[x][y] == '1':
            d = 3
        elif matrix[x][y] == '4':
            d = 2

    elif d == 1:
        if matrix[x][y] in ['|', '+']:
            d = 1
        elif matrix[x][y] == '2':
            d = 3
        elif matrix[x][y] == '3':
            d = 2
    elif d == 2:
        if matrix[x][y] in ['-', '+']:
            d = 2
        elif matrix[x][y] == '1':
            d = 1
        elif matrix[x][y] == '2':
            d = 0
    elif d == 3:
        if matrix[x][y] in ['-','+']:
            d = 3
        elif matrix[x][y] == '3':
            d = 0
        elif matrix[x][y] == '4':
            d = 1

    next_x = x + dx[d]
    next_y = y + dy[d]
    return next_x, next_y, d


def get_last_block(Md, Zd):
    if Md == 0 and Zd == 1 or Md == 1 and Zd == 0:
        return '|'
    elif Md == 2 and Zd == 3 or Md == 3 and Zd == 2:
        return '-'
    elif Md == 0 and Zd == 2 or Md == 2 and Zd == 0:
        return '1'
    elif Md == 1 and Zd == 2 or Md == 2 and Zd == 1:
        return '2'
    elif Md == 3 and Zd == 1 or Md == 1 and Zd == 3:
        return '3'
    elif Md == 3 and Zd == 0 or Md == 0 and Zd == 3:
        return '4'


if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    # print_matrix(matrix)

    passage_count = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != '.':
                passage_count += 1
            if matrix[i][j] == 'M':
                M_x = i
                M_y = j
            elif matrix[i][j] == 'Z':
                Z_x = i
                Z_y = j

    next_x, next_y, d = get_starting_point(M_x, M_y)
    # print('M start')
    # print(next_x, next_y, d)
    M_dq.append((next_x, next_y, d))

    next_x, next_y, d = get_starting_point(Z_x, Z_y)
    # print('Z start')
    # print(next_x, next_y, d)
    Z_dq.append((next_x, next_y, d))

    M_count = 1
    while M_dq:
        x, y, d = M_dq.popleft()
        if visited[x][y] is False:
            visited[x][y] = True
            M_count += 1
        # print(x,y,d)
        nx, ny, nd = get_next_xy(x, y, d)
        if matrix[nx][ny] == '.':
            break
        else:
            M_dq.append((nx, ny, nd))
    # print('M dq last : ', nx, ny, nd)
    Mx = nx
    My = ny
    Md = nd

    Z_count = 1
    while Z_dq:
        x, y, d = Z_dq.popleft()
        if visited[x][y] is False:
            visited[x][y] = True
            Z_count += 1
        nx, ny, nd = get_next_xy(x, y, d)
        if matrix[nx][ny] == '.':
            break
        else:
            Z_dq.append((nx, ny, nd))
    # print('Z dq last : ', nx, ny, nd)
    Zx = nx
    Zy = ny
    Zd = nd

    # print('passage_count : ', passage_count)
    # print('M count : ', M_count)
    # print('Z count : ', Z_count)

    last_d = get_last_block(Md, Zd)
    if M_count + Z_count != passage_count:
        last_d = '+'
    print(Zx+1, Zy+1, last_d)

