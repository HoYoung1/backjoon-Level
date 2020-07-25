from copy import deepcopy

total = 0

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]

    dp = deepcopy(matrix)

    result = 0

    for j in range(1, N):
        for i in range(M):
            for k in range(M):
                if i == k:
                    dp[i][j] = max(dp[i][j], matrix[i][j]//2 + dp[k][j-1])
                else:
                    dp[i][j] = max(dp[i][j], matrix[i][j] + dp[k][j - 1])

    for row in dp:
        result = max(result, max(row))

    print(result)



