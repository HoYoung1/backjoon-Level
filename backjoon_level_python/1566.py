from copy import deepcopy


def solve2(N, M, matrix):
    answer = 0

    while True:
        minus_idx, zero_flag = get_minus_sum_row_or_col(M, N, matrix)
        if len(minus_idx) == 0:
            if zero_flag:
                return -1
            else:
                return answer

        minus_idx.sort(key=lambda x: x[2])
        for d, idx, _ in minus_idx:
            arr = deepcopy(matrix)
            if d == 'r':
                for i in range(M):
                    arr[idx][i] = matrix[idx][i] * -1
            elif d == 'c':
                for i in range(N):
                    arr[i][idx] = matrix[i][idx] * -1
            print('뒤집은 arr', arr)

            _, zero_flag = get_minus_sum_row_or_col(M, N, arr)
            if zero_flag:
                continue
            else:
                matrix = arr
                break
        else:
            return -1
        answer += 1


def get_minus_sum_row_or_col(M, N, matrix):
    minus_idx = []
    zero_flag = False
    for i in range(N):
        sum_row = sum(matrix[i])
        if sum_row < 0:
            minus_idx.append(('r', i, sum_row))
        elif sum_row == 0:
            zero_flag = True

    for i in range(M):
        sum_col = sum(row[i] for row in matrix)
        if sum_col < 0:
            minus_idx.append(('c', i, sum_col))
        elif sum_col == 0:
            zero_flag = True
    return minus_idx, zero_flag


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(solve2(N, M, matrix))

    mat = [[1, 3, 1], [-1, 9, 2]]
    print(solve2(len(mat), len(mat[0]), mat))

    mat = [[30, -1, -2], [0, 1, 1]]
    print(solve2(len(mat), len(mat[0]), mat))

    mat = [[-9, 1, 2], [34, 3, 30], [-5, 9, 29]]
    print(solve2(len(mat), len(mat[0]), mat))

    mat = [[-4, 1], [6, -7]]
    print(solve2(len(mat), len(mat[0]), mat))

    mat = [[-7, 8, 9], [9, 3, 8], [-1, 6, -1]]
    print(solve2(len(mat), len(mat[0]), mat))

    mat = [[1, 0], [0, -1]]
        print(solve2(len(mat), len(mat[0]), mat))

    mat = [[-1, -4, 11, 12], [3, 2, -7, -15], [8, -5, -6, 14], [-16, 9, 10, -13]]
    print(solve2(len(mat), len(mat[0]), mat))
