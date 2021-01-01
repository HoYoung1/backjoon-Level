import sys
import heapq

input = sys.stdin.readline


def solve(N):
    hq = []

    while N:
        input_num = int(input().rstrip())
        if input_num == 0:
            if hq:
                print(heapq.heappop(hq)[1])
            else:
                print(0)
        else:
            heapq.heappush(hq, (abs(input_num), input_num))
        N -= 1


if __name__ == '__main__':
    N = int(input().rstrip())

    solve(N)