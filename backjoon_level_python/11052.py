def solve(N, P):
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, i+1):
            # print('i, j',i, j)
            dp[i] = max(dp[i-j] + P[j], dp[i])
    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    P = [0] + list(map(int, input().split()))

    print(solve(N, P))