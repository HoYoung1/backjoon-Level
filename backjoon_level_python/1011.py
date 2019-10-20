# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 3
# 5 -> 4
# 6 -> 4
# 7 -> 5
# 8 -> 5
# 9 -> 5
#
# #
# 1 -> 1            1
# 4 -> 121          3
# 9 -> 12321        5
# 16-> 1234321      7
# 25 -> 123454321   9
#
# 2 -> 11           2
# 6 -> 1221         4
# 12 -> 123321      6
# 20 -> 12344321    8
# 30 -> 1234554321  10

import sys
import math
# x면 x보다 큰 수를 찾고 그 수의 자리수를 리턴하면됨.




def fly(x,y):
    max_int = 2**32
    pre_dist = [2]
    import sys

    for i in range(2, sys.maxsize):
        num = pre_dist[-1] + i * 2
        if num + i * 2 > 2 ** 31:
            break
        pre_dist.append(num)
    for i in range(1, sys.maxsize):
        if pre_dist[-1] > 2 ** 31:
            break
        pre_dist.append(i ** 2)

    pre_dist.sort()

    sub = y - x
    rtn = None
    for idx, item in enumerate(pre_dist):
        if item >= sub:
            rtn = idx+1
            break
    return rtn




def test_fly():
    assert fly(0, 1) == 1
    assert fly(0, 3) == 3
    assert fly(1, 5) == 3
    assert fly(45, 50) == 4
    assert fly(45, 51) == 4
    assert fly(45, 52) == 5
    assert fly(45, 54) == 5
    assert fly(45, 57) == 6
    assert fly(45, 58) == 7

if __name__ == '__main__':
    for i in range(int(input())):
        a, b = map(int,input().split())
        print(fly(a,b))