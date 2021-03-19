# 원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합

# 원의 넓이 : pi * r * r
# 두 점 사이의 거리 sqrt of (x2-x1) ** 2 + (y2-y1) ** 2
# 택시 기하학(taxi cab geometry) : D(T1,T2) = |x1-x2| + |y1-y2|

import math

if __name__ == '__main__':
    R = int(input())
    print('{:.6f}'.format(math.pi * R * R))
    print('{:.6f}'.format((2 * R ** 2)))
