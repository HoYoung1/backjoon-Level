# dp[a][b] = a~b까지 끼워 넣어야하는 최소갯수
import sys
sys.setrecursionlimit(10**8)



def solve(N, numbers):
    return rec(0, len(numbers)-1)


def rec(a, b):
    # print(a, b)
    if a > b:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    if numbers[a] == numbers[b]:
        dp[a][b] = rec(a+1, b-1)
        return dp[a][b]
    dp[a][b] = min(rec(a, b-1) + 1, rec(a+1, b) + 1)
    return dp[a][b]


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))

    dp = [[-1] * len(numbers) for _ in range(len(numbers))]
    print(solve(N, numbers))

