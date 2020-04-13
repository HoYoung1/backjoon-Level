# https://www.acmicpc.net/problem/6603
# 29284KB 60ms
from itertools import combinations

if __name__ == '__main__':
    LOTTO_LENGTH = 6

    while True:
        S = input().split()
        if S == ['0']:
            break

        S = list(map(int, S[1:]))
        for comb in combinations(S, LOTTO_LENGTH):
            print(' '.join(map(str, comb)))
        print()


