import bisect
import sys
input = sys.stdin.readline


def solve(N, H, bottom, top):
    answer = sys.maxsize
    answer_count = -1

    bottom.sort()
    top.sort()
    print(bottom)
    print(top)

    for i in range(1, H+1):
        idx = bisect.bisect_left(bottom, i)
        temp = len(bottom) - idx

        idx = bisect.bisect_right(top, H-i)
        temp += len(top) - idx

        if answer > temp:
            answer = temp
            answer_count = 1
        elif answer == temp:
            answer_count += 1
    return answer, answer_count


if __name__ == '__main__':
    N, H = map(int, input().rstrip().split())
    bottom = []
    top = []
    for i in range(N):
        if i % 2 == 0:
            bottom.append(int(input().rstrip()))
        else:
            top.append(int(input().rstrip()))
    print(' '.join(map(str, solve(N, H, bottom, top))))