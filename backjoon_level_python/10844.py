def solve(N):
    dp = [[0]*10 for _ in range(N+1)]

    # dp[N][L] = 길이 N 일 때, 마지막 자리 수가 L 일 경우의 계단 수

    for i in range(1, 10):
        dp[1][i] = 1

    for n in range(2,N+1):
        for l in range(0,10):
            if l == 0:
                dp[n][l] = dp[n-1][l+1]
            elif l == 9:
                dp[n][l] = dp[n-1][l-1]
            else:
                dp[n][l] = dp[n-1][l-1] + dp[n-1][l+1]

    # for row in dp:
    #     print(row)
    # print(row)
    #
    print(sum(dp[N])%1000000000)




if __name__ == '__main__':
    N = int(input())
    solve(N)