import re


if __name__ == '__main__':
    p = re.compile('(100+1+|01)+')

    a = input()
    if p.fullmatch(a):
        print('SUBMARINE')
    else:
        print('NOISE')
