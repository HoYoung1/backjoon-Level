# def solve(N, numbers):
#     """
#     x = 수열 A의 크기
#     arr = 수열 A를 이루고 있는 A(i)를 담은 배열
#     dp = arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
#     """
#     dp = [1] * N
#     for i in range(N):
#         for j in range(i):
#             if numbers[i] > numbers[j] and dp[i] <= dp[j]:
#                 dp[i] = dp[j] + 1
#     return dp
import bisect


def solve(N, arr):
    dp = [arr[0]]
    for i in range(N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    return len(dp)


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    print(solve(N, numbers))

