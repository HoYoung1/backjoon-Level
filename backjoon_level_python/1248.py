import sys


def get_sign(num):
    if num > 0:
        return '+'
    elif num < 0:
        return '-'
    elif num == 0:
        return '0'


def is_valid(A_list):
    length = len(A_list)
    idx = length-1
    for i in range(length):
        if encodings[idx] != get_sign(sum(A_list[i:])):
            return False
        idx += N-i-1
    return True


def dfs(depth):
    if depth == N:
        # this is answer
        for A in A_list:
            print(A, end=' ')
        sys.exit(0)

    for i in range(-10, 11, 1):
        if is_valid(A_list + [i]):
            A_list.append(i)
            dfs(depth + 1)
            A_list.pop()


if __name__ == '__main__':
    N = int(input())  # N은 10보다 작거나 같은 자연수이다
    encodings = input()
    A_list = []
    dfs(0)
