import sys
input = sys.stdin.readline

def find(s, e):
    if dp[s][e] != sys.maxsize:
        return dp[s][e]
    if s == e:
        return 0
    for m in range(s, e):
        dp[s][e] = min(dp[s][e], find(s, m) + find(m + 1, e) + abs(min(numbers[s:m + 1]) - min(numbers[m + 1:e + 1])))
    return dp[s][e]


def solve(n, numbers):
    return find(0, n-1)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [[sys.maxsize]*n for _ in range(n)]
    print(solve(n, numbers))
