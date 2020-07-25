import sys
sys.setrecursionlimit(10**7)


def min_recur(num, dp):
    m = sys.maxsize

    if dp[num] != -1 or num == 1:
        return dp[num]

    if num % 3 == 0:
        m = min(m, min_recur(num//3,dp))
    if num % 2 == 0:
        m = min(m, min_recur(num//2,dp))
    m = min(m, min_recur(num - 1, dp))
    dp[num] = m+1
    return dp[num]


def solve(num):
    dp = [-1] * 1000001
    dp[1] = 0
    min_recur(num,dp)
    return dp[num]


def solve2(num):
    dp = [0] * 1000001
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 1000001):
        c = sys.maxsize
        if i%3 == 0:
            c = min(c, dp[i//3] + 1)
        if i%2 == 0:
            c = min(c, dp[i//2] + 1)
        c = min(c, dp[i-1]+1)
        dp[i] = c
    return dp[num]


if __name__ == '__main__':
    num = int(input())

    print(solve(num))