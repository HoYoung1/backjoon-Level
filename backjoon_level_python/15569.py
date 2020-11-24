def solve(N, M):
    dp = [0]*(M+1)
    dp[0], dp[1] = 0, 1

    temp = 2 ** (N - 1) - 1
    for i in range(2, M+1):
        for j in range(1, N+1):
            if i-j == 0:
                dp[i] += 1
            elif i-j > 0:
                dp[i] += dp[i-j]
        if i >= N:
            dp[i] += temp if i-N == 0 else dp[i-N] * temp

    print(dp)
    return dp[M]


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M) % 1999)
