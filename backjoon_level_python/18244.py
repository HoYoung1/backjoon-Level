def solve(N):
    dp = [[[0]*6 for _ in range(10)] for _ in range(N+1)]
    mod = 1000000007

    # dp[N][L] : 자릿수 N이면서 , 마지막 자리가 L 일 경우 변형 계단의 수
    # dp[N][L] = dp[N-1][L-1] + dp[N-1][L+1]

    # dp[N][L][D] : 자릿수 N이면서 , 마지막 자리가 L이면서, 깊이가 D인 변형 계단의 수
    # D 정의 :
    # 1 2번감소
    # 2 1번감소
    # 3 0번
    # 4 1번증가
    # 5 2번증가1

    mid = 3

    # 초기화
    for i in range(10):
        dp[1][i][mid] = 1
    for i in range(10):
        if i == 0:
            dp[2][i][mid-1] = dp[1][i + 1][mid]
        elif i == 9:
            dp[2][i][mid+1] = dp[1][i - 1][mid]
        else:
            dp[2][i][mid+1] = dp[1][i-1][mid]
            dp[2][i][mid-1] = dp[1][i+1][mid]
    # for row in dp:
    #     print(row)
    # print()

    # DP 점화식

    for i in range(3, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j][mid-1] = dp[i - 1][j + 1][mid+1]% mod
                dp[i][j][mid-2] = dp[i - 1][j + 1][mid-1]% mod
            elif j == 9:
                dp[i][j][mid+1] = dp[i - 1][j - 1][mid-1]% mod
                dp[i][j][mid+2] = dp[i - 1][j - 1][mid+1]% mod
            else:
                dp[i][j][mid+1] = dp[i-1][j-1][mid-1] + dp[i-1][j-1][mid-2]% mod
                dp[i][j][mid+2] = dp[i-1][j-1][mid+1]% mod
                dp[i][j][mid-1] = dp[i-1][j+1][mid+1] + dp[i-1][j+1][mid+2]% mod
                dp[i][j][mid-2] = dp[i-1][j+1][mid-1]% mod
    answer = 0
    for row in dp[N]:
        answer += sum(row)
        answer %= mod

    return answer % mod








if __name__ == '__main__':
    N = int(input())
    if N == 1:
        print(10)
    else:
        print(solve(N))