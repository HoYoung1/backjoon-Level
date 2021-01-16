import sys
from math import sqrt
from itertools import combinations

input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        P_num = int(input())
        P = [list(map(int, input().split())) for _ in range(P_num)]

        total = [0, 0]
        for p in P:
            total[0], total[1] = total[0]+p[0], total[1]+p[1]

        result = sys.maxsize
        for comb in combinations(P, len(P)//2):
            pos = [0, 0]
            neg = [total[0], total[1]]

            for x, y in comb:
                pos[0], pos[1] = pos[0]+x, pos[1]+y
                neg[0], neg[1] = neg[0]-x, neg[1]-y
            temp = sqrt((pos[0] - neg[0]) * (pos[0] - neg[0]) + (pos[1] - neg[1]) * (pos[1] - neg[1]))
            result = min(result, temp)
        print(result)


