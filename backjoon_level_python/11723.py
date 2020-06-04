# https://www.acmicpc.net/problem/11723
# 29380KB 5220ms
import sys

if __name__ == '__main__':
    M = int(input())
    S = set()
    for i in range(M):
        input_text = sys.stdin.readline().strip()
        if input_text == 'all' or input_text == 'empty':
            order = input_text
        else:
            order, value = input_text.split()
            value = int(value)
        if order == 'add':
            S.add(value)
        elif order == 'remove':
            if value in S:
                S.remove(value)
        elif order == 'check':
            if value in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if value in S:
                S.remove(value)
            else:
                S.add(value)
        elif order == 'all':
            S = {i for i in range(1, 21)}
        elif order == 'empty':
            S = set()
