import sys
sys.setrecursionlimit(10**8)


def solve(t1, t2):
    return lcs(len(t1), len(t2))


def lcs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == 0 or y == 0:
        dp[x][y] = 0
        return 0
    if t1[x-1] == t2[y-1]:
        dp[x][y] = lcs(x-1, y-1) + 1
        return dp[x][y]
    else:
        dp[x][y] = max(lcs(x-1, y), lcs(x, y-1))
        return dp[x][y]


if __name__ == '__main__':
    t1 = input()
    t2 = input()
    dp = [[-1] * (len(t2)+1) for _ in range(len(t1)+1)]
    print(solve(t1, t2))