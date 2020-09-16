import sys
input = sys.stdin.readline


def all_same(n, matrix):
    init = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != init:
                return False
    return True


def divide(n, matrix):
    if all_same(n, matrix):
        count_dict[matrix[0][0]] += 1
        return

    cut_range = n // 3
    divide(cut_range, [row[cut_range * 0:cut_range * 1] for row in matrix[cut_range * 0:cut_range * 1]])
    divide(cut_range, [row[cut_range * 1:cut_range * 2] for row in matrix[cut_range * 0:cut_range * 1]])
    divide(cut_range, [row[cut_range * 2:cut_range * 3] for row in matrix[cut_range * 0:cut_range * 1]])
    divide(cut_range, [row[cut_range * 0:cut_range * 1] for row in matrix[cut_range * 1:cut_range * 2]])
    divide(cut_range, [row[cut_range * 1:cut_range * 2] for row in matrix[cut_range * 1:cut_range * 2]])
    divide(cut_range, [row[cut_range * 2:cut_range * 3] for row in matrix[cut_range * 1:cut_range * 2]])
    divide(cut_range, [row[cut_range * 0:cut_range * 1] for row in matrix[cut_range * 2:cut_range * 3]])
    divide(cut_range, [row[cut_range * 1:cut_range * 2] for row in matrix[cut_range * 2:cut_range * 3]])
    divide(cut_range, [row[cut_range * 2:cut_range * 3] for row in matrix[cut_range * 2:cut_range * 3]])


def solve(N, matrix):
    divide(N, matrix)


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    count_dict = {
        -1: 0,
        0: 0,
        1: 0
    }

    solve(N, matrix)
    for k, v in count_dict.items():
        print(v)

    # assert all_same(3, [[0, 1, -1], [0, -1, 1], [0, 1, -1]]) is False