

if __name__ == '__main__':
    T = int(input())

    dp = [-1] * 101
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4, 101):
        dp[i] = dp[i-3] + dp[i-2]
    for i in range(T):
        print(dp[int(input())])