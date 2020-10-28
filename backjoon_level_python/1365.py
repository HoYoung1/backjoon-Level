from bisect import bisect


def solve(N, numbers):
    dp = []
    for num in numbers:
        k = bisect(dp, num)
        if k >= len(dp): # TODO : check
            dp.append(num)
        else:
            dp[k] = num
    answer = len(dp)
    return answer


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    print(N - solve(N, numbers))