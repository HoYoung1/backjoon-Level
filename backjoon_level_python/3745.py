import sys
import bisect


def solve1():
    while True:
        N = int(input())
        numbers = list(map(int, input().split()))
        dp = [1] * N
        max_value = 1
        for i in range(N):
            for j in range(0, i):
                if numbers[j] < numbers[i]:
                    dp[i] = dp[j] + 1
                    max_value = max(max_value, dp[i])
        print(max_value)


def solve2():
    while True:
        N = int(input())
        numbers = list(map(int, input().split()))
        making_lis = [sys.maxsize]
        max_value = 1
        for i in range(N):
            if making_lis[-1] < numbers[i]:
                making_lis.append(numbers[i])
                max_value += 1
            else:
                a = bisect.bisect_left(making_lis, numbers[i])
                making_lis[a] = numbers[i]
            # print(making_lis)
        print(max_value)


if __name__ == '__main__':
    try:
        # solve1()
        solve2()
    except:
        exit(0)