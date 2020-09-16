
def solve(n, k, coins):
    pass

# dp = [[sys.maxsize] * (k+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1, k+1):
#         num_coins = j // coins[i]
#         if j % coins[i] != 0:
#             num_coins = num_coins + dp[i][j % coins[i]]
#         else:
#             dp[i][j] = num_coins
#         dp[i][j] = min(dp[i-1][j], num_coins)

# for row in dp:
#     print(row)
# print()

import sys

if __name__ == '__main__':
    n, k = map(int, input().split())
    # coins = [-1] + sorted([int(input()) for _ in range(n)])
    coins = [-1] + [int(input()) for _ in range(n)]

    dp = [[0] + [sys.maxsize] * k for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, k+1):
            if j-coins[i] >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    if dp[n][k] == sys.maxsize:
        print(-1)
    else:
        print(dp[n][k])
