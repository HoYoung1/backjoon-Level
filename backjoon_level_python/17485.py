import sys


def solve(N, M, matrix):
    dp = [[[sys.maxsize] * 3 for _ in range(M)]  for _ in range(N)]

    # init
    for idx, cost in enumerate(matrix[0]):
        dp[0][idx][0] = cost
        dp[0][idx][1] = cost
        dp[0][idx][2] = cost
    dp[0][0][0] = sys.maxsize
    dp[0][-1][2] = sys.maxsize

    for i in range(1, N):
        for j in range(M):
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + matrix[i][j] if j != 0 else sys.maxsize
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + matrix[i][j]
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + matrix[i][j] if j != M-1 else sys.maxsize

    # find answer
    answer = sys.maxsize
    for row in dp[-1]:
        answer = min(answer, min(row))
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    print(solve(N, M, matrix))