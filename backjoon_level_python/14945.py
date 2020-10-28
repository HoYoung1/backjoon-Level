def solve(n):
    # DP[타일 수][두 사람의 거리] = 조건에서 안전하게 빠져나가는 경우의 수
    dp = [[0] * (n+2) for _ in range(n+2)]
    dp[2][1] = 2
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i][j] = (dp[i-1][j] * 2 + dp[i-1][j-1] + dp[i-1][j+1]) % 10007

    answer = 0
    # for row in dp:
    #     print(row)
    # print()

    for i in range(1, n):
        answer += dp[n][i]
    return answer % 10007



if __name__ == '__main__':
    n = int(input())
    print(solve(n))