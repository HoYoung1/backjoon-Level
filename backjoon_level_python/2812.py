from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    answer_length = N-K
    num = input()

    dq = deque()
    for n in num:
        while K and dq and dq[-1] < n:
            K -= 1
            dq.pop()
        dq.append(n)

    print(''.join(dq)[:answer_length])




