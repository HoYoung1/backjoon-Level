import sys


def solve(N, matrix):
    dp = [[0]*N for _ in range(N)]

    for x in range(1, N):  # 거리가 x인 것까지
        for i in range(N - x):  # i부터 시작
            j = i + x
            dp[i][j] = sys.maxsize
            for k in range(i, j):  # 두 행렬의 곱에서 나오는 추가비용계산해서 더해주기
                dp[i][j] = min(dp[i][j],
                               dp[i][k] + dp[k + 1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1]))

    return dp[0][N-1]


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, matrix))

