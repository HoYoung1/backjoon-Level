# dp[x] = x 자리에서 끝나는 연속된 수들의
def solve(n, numbers):
    dp = [-1] * n
    dp[0] = numbers[0]
    for i in range(1, n):
        dp[i] = max(numbers[i], dp[i-1] + numbers[i])
    return max(dp)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(solve(n, numbers))