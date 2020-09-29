def get_col_sum(idx):
    result = 0
    for row in matrix:
        result += int(row[idx])
    return result


def get_row_sum(idx):
    return sum(map(int, matrix[idx]))


def solve(N, M, matrix):
    answer = 0

    # 가로방향
    first_sum = 0
    for i in range(M-2):
        first_sum += get_col_sum(i)

        second_sum = 0
        for j in range(i+1, M-1):
            second_sum += get_col_sum(j)

            third_sum = 0
            for k in range(j+1, M):
                third_sum += get_col_sum(k)
                if k == M-1:
                    answer = max(answer, first_sum * second_sum * third_sum)
    # 세로방향
    first_sum = 0
    for i in range(N-2):
        first_sum += get_row_sum(i)

        second_sum = 0
        for j in range(i+1, N-1):
            second_sum += get_row_sum(j)

            third_sum = 0
            for k in range(j+1, N):
                third_sum += get_row_sum(k)
                if k == N-1:
                    answer = max(answer, first_sum * second_sum * third_sum)

    # 가로방향, 오른쪽 위아래가 쪼개짐
    first_sum = 0
    for i in range(M):
        first_sum += get_col_sum(i)

        second_sum = 0
        for j in range(N-1):
            second_sum += sum(map(int, matrix[j][i+1:]))

            third_sum = 0
            for k in range(j + 1, N):
                third_sum += sum(map(int, matrix[k][i+1:]))
                if k == N - 1:
                    answer = max(answer, first_sum * second_sum * third_sum)

    # 가로방향, 왼쪽 위아래가 쪼개짐
    first_sum = 0
    for i in range(M-1, -1, -1):
        first_sum += get_col_sum(i)

        second_sum = 0
        for j in range(N-1):
            second_sum += sum(map(int, matrix[j][:i]))

            third_sum = 0
            for k in range(j+1, N):
                third_sum += sum(map(int, matrix[k][:i]))
                if k == N - 1:
                    answer = max(answer, first_sum * second_sum * third_sum)

    # 세로방향, 아래쪽 좌우가쪼개짐
    first_sum = 0
    for i in range(N):
        first_sum += get_row_sum(i)

        second_sum = 0
        for j in range(M-1):
            second_sum += sum([int(matrix[e][j]) for e in range(i+1, N)])

            third_sum = 0
            for k in range(j + 1, M):
                third_sum += sum([int(matrix[e][k]) for e in range(i+1, N)])
                if k == M - 1:
                    answer = max(answer, first_sum * second_sum * third_sum)

    # 세로방향, 위쪽 좌우가쪼개짐
    first_sum = 0
    for i in range(N-1, -1, -1):
        first_sum += get_row_sum(i)

        second_sum = 0
        for j in range(M):
            second_sum += sum([int(matrix[e][j]) for e in range(0, i)])

            third_sum = 0
            for k in range(j + 1, M):
                third_sum += sum([int(matrix[e][k]) for e in range(0, i)])
                if k == M - 1:
                    answer = max(answer, first_sum * second_sum * third_sum)


    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    print(solve(N, M, matrix))