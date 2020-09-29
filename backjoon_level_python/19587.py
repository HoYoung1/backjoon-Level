def solve(N):
    dp = [[[0] * 2 for _ in range(2)] for _ in range(N)]
    # dp[N][2][2]

    dp[0][0][0] = 1
    dp[0][0][1] = 1
    dp[0][1][0] = 1

    mod = 10**9 + 7

    for i in range(1, N):
        dp[i][0][1] = dp[i-1][1][0] + dp[i-1][0][0]
        dp[i][1][0] = dp[i-1][0][1] + dp[i-1][0][0]
        dp[i][0][0] = dp[i-1][1][0] + dp[i-1][0][1] + dp[i-1][0][0]
    return (dp[N-1][0][0] + dp[N-1][0][1] + dp[N-1][1][0]) % mod


if __name__ == '__main__':
    N = int(input())
    print(solve(N))