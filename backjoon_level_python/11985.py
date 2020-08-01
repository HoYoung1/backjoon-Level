import sys

input = sys.stdin.readline


def solve3(N, M, K, oranges):
    dp = [sys.maxsize] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        # init
        max_value = -sys.maxsize
        min_value = sys.maxsize
        for j in range(i, i-M, -1):
            if j < 1:
                break

            if oranges[j] > max_value:
                max_value = oranges[j]
            if oranges[j] < min_value:
                min_value = oranges[j]

            dp[i] = min(dp[i], dp[j-1] + (max_value - min_value) * (i - j + 1) + K)
    return dp[-1]


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    oranges = [0] + [int(input()) for i in range(N)]

    print(solve3(N, M, K, oranges))