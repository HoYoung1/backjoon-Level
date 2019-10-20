# 노트북의 갯수 x 라고 생각하자
import math


def breakeven_point(a, b, c):
    # a + (b * x) == c * x # 1000 + 70x = 170x = 170x - 70x = 1000
    if b < c:
        return math.floor((a/(c-b))+1)
    return -1


def test_find_breakeven_point():
    assert breakeven_point(1000, 70, 170) == 11


a, b, c = map(int, input().split())
print(breakeven_point(a, b, c))

