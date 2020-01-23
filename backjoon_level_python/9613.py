# GCD 합
# https://www.acmicpc.net/problem/9613

from itertools import combinations
from math import gcd

if __name__ == '__main__':
    for i in range(int(input())):
        input_num = input().split()
        nums = list(map(int, input_num[1:]))
        # print(nums)

        gcd_list = []
        for a, b in combinations(nums, 2):
            gcd_value = gcd(a, b)
            gcd_list.append(gcd_value)

        print(sum(gcd_list))



"""
3
4 10 20 30 40
3 7 5 12
3 125 15 25
"""
