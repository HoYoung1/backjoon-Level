def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def check(i, j, k, l):
    for a in range(i, k+1):
        for b in range(j, l+1):
            if matrix[a][b] == 0:
                return False
    return True


def solve(matrix):
    max_area = -1
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 0:
                continue

            for k in range(i+1, 100):
                for l in range(j+1, 100):
                    if matrix[k][l] == 0:
                        continue

                    area = (k - i + 1) * (l - j + 1)
                    if area < max_area:
                        continue

                    if check(i, j, k, l):
                        max_area = max(max_area, area)
                    else:
                        break
    return max_area


if __name__ == '__main__':
    n = int(input())
    matrix = [[0] * 100 for _ in range(100)]
    for i in range(n):
        a, b = map(int, input().split())

        # draw
        for j in range(b, b + 10):
            for k in range(a, a +10):
                matrix[j][k] += 1
        # print_matrix(matrix)

    print(solve(matrix))
