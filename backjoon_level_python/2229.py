import sys


def solve(N, numbers):
    dp = [0] * (N+1) # dp[i] = max(dp[j - 1] + (i ~ j 까지 조 짜기 점수
    for i in range(1,N+1):
        maximum = 0
        minimum = sys.maxsize
        for j in range(i, 0, -1):
            maximum = max(maximum, numbers[j-1])
            minimum = min(minimum, numbers[j-1])
            dp[i] = max(dp[j-1] + (maximum-minimum), dp[i])

    return dp[N]


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    print(solve(N, numbers))

    assert solve(1, list(map(int, '2'.split()))) == 0
    assert solve(3, list(map(int, '2 5 7'.split()))) == 5
    assert solve(2, list(map(int, '2 5'.split()))) == 3
    assert solve(10, list(map(int, '2 5 7 1 3 4 8 6 9 3'.split()))) == 20
