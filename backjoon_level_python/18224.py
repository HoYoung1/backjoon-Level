import sys
from collections import deque

# 북, 남, 좌,
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline


def check_day_or_night(day_count):
    if (day_count // m) % 2 == 0:
        return False
    return True


def get_next_x_y(x, y, i):
    next_x = x + dx[i]
    next_y = y + dy[i]
    while True:
        if matrix[next_x][next_y] != 1:
            break
        next_x = next_x + dx[i]
        next_y = next_y + dy[i]
    return next_x, next_y


def get_answer_by_daycount(day_count):
    day = day_count // (m * 2) + 1
    dat_text = check_day_or_night(day_count)
    if dat_text is False:
        dat_text = 'sun'
    else:
        dat_text = 'moon'
    return '{} {}'.format(day, dat_text)


def solve(n, m, matrix):
    min_day_count = sys.maxsize
    visited = [[[[False]*99999 for _ in range(2)] for _ in range(n)] for _ in range(n)]

    dq = deque()
    dq.append((0, 0, 0))
    visited[0][0][False][0] = True
    while dq:
        x, y, day_count = dq.popleft()
        is_moon = check_day_or_night(day_count)
        if x == n - 1 and y == n - 1:
            # find answer
            print(x, y, day_count)
            min_day_count = min(min_day_count, day_count)
        if not is_moon:  # 낮이라면
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y][is_moon][day_count+1] is False and matrix[next_x][
                    next_y] != 1:
                    visited[next_x][next_y][is_moon][day_count+1] = True
                    if next_x == 2 and next_y == 4:
                        print(3)
                    dq.append((next_x, next_y, day_count + 1))
        else:  # 밤이라면
            for i in range(4):
                try:
                    next_x, next_y = get_next_x_y(x, y, i)
                except:
                    # print('범위아웃, 벽 못넘음^^')
                    continue
                if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y][is_moon][day_count+1] is False and matrix[next_x][
                    next_y] != 1:
                    visited[next_x][next_y][is_moon][day_count+1] = True
                    if next_x == 2 and next_y == 4:
                        print(3)
                    dq.append((next_x, next_y, day_count + 1))

    if min_day_count != sys.maxsize:
        answer = get_answer_by_daycount(min_day_count)
    else:
        answer = -1
    return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, matrix))

    # matrix = [
    #     [0, 0, 0, 1, 1, 0],
    #     [1, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 1, 1],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0]
    # ]
    # m = 2
    # print(solve(len(matrix), m, matrix))

    # matrix = [
    #     [0, 0, 0, 1, 1, 0],
    #     [1, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1],
    #     [0, 0, 0, 0, 1, 1],
    #     [0, 1, 1, 1, 1, 0]
    # ]
    # m = 2
    # print(solve(len(matrix), m, matrix))

    # matrix = [
    #     [0, 0, 0, 1, 0, 0],
    #     [1, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1],
    #     [0, 1, 1, 0, 1, 1],
    #     [0, 1, 1, 1, 1, 0]
    # ]
    # m = 2
    # print(solve(len(matrix), m, matrix))

    matrix = [
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0]
    ]
    m = 2
    print(solve(len(matrix), m, matrix))
