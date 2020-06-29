# 시간초과
import time


def solve():
    visited = 1

    l = []
    for _ in range(n):
        temp = int(input())
        l.append(temp)
        visited = visited | 1 << temp  # 비트마스킹
    l.sort()

    for num in l[:len(l) // 2]:
        another_lego = target - num
        if visited & 1 << another_lego: # 비트체크
            return 'yes {} {}'.format(num, another_lego)
    else:
        return 'danger'


def solve2():
    l = []
    for _ in range(n):
        temp = int(input())
        l.append(temp)
    l.sort()

    p1, p2 = 0, len(l)-1

    target = x * 10000000
    while p1<p2:
        if target > l[p2] + l[p1]:
            p1 += 1
        elif target < l[p2] + l[p1]:
            p2 -= 1
        else:
            return 'yes {} {}'.format(l[p1], l[p2])
    return 'danger'






if __name__ == '__main__':
    try:
        while True:
            x = int(input()) # 단위는 센티미터
            target = x * 10000000
            n = int(input()) # (0 ≤ n ≤ 1000000)

            start = time.time()
            print(solve2())
            print(time.time()-start)
    except:
        exit()


    
