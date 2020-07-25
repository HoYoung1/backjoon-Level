# https://www.acmicpc.net/problem/1013
# https://nerogarret.tistory.com/30 참고함..

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        text = input()
        p = re.compile('(100+1+|01)+')
        if p.fullmatch(text):
            print('YES')
        else:
            print('NO')
