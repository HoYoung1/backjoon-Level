def solve(N):
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N+1):
        # print(i)
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[N]


if __name__ == '__main__':
    N = int(input())
    dp = [-1] * (N+1)
    print(solve(N-1))