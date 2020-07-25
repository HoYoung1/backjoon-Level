import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def find(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    if s == e:
        dp[s][e] = 1
        return dp[s][e]
    if numbers[s] != numbers[e]:
        dp[s][e] = 0
        return dp[s][e]
    if s == e - 1:
        dp[s][e] = 1
        return dp[s][e]
    dp[s][e] = find(s + 1, e - 1)
    return dp[s][e]


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())

    dp = [[-1]*N for _ in range(N)]

    for i in range(M):
        S, E = map(int, input().split())
        print(find(S-1, E-1))