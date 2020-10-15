import sys
input = sys.stdin.readline

import bisect

def solve(num_list):
    # print(num_list)
    dp = []
    for num in num_list:
        idx = bisect.bisect_left(dp, num)
        if len(dp) <= idx:
            dp.append(num)
        else:
            dp[idx] = num

    return len(dp)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(T):
        value_num = int(input().rstrip())
        values = [int(input().rstrip()) for j in range(value_num)]
        print(solve(values))