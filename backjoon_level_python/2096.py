import sys

if __name__ == '__main__':
    N = int(input())
    a, b, c = map(int, input().split())
    dp = [[a, a], [b, b], [c, c]]
    for i in range(N-1):
        a, b, c = map(int, input().split())

        t1 = max(dp[0][0], dp[1][0]) + a
        t2 = min(dp[0][1], dp[1][1]) + a

        t3 = max(dp[0][0], dp[1][0], dp[2][0]) + b
        t4 = min(dp[0][1], dp[1][1], dp[2][1]) + b

        t5 = max(dp[1][0], dp[2][0]) + c
        t6 = min(dp[1][1], dp[2][1]) + c

        dp = [[t1,t2], [t3,t4], [t5,t6]]

    max_value = 0
    min_value = sys.maxsize
    for j in range(3):
        for k in range(2):
            max_value = max(max_value, dp[j][k])
            min_value = min(min_value, dp[j][k])

    print('{} {}'.format(max_value, min_value))
