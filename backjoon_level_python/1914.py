import sys
sys.setrecursionlimit(10**8)

answer = 0
path = []


def solve(K):
    global answer
    if K<=20:
        hanoi(K, 1, 3, 2)
    else:
        answer = 2**K-1
    return answer


def hanoi(disk_num, start, end, assitant):
    global answer, path

    if disk_num == 1:
        answer += 1
        path.append((start, end))
        return
    hanoi(disk_num - 1, start, assitant, end)
    answer += 1
    path.append((start, end))
    hanoi(disk_num - 1, assitant, end, start)


if __name__ == '__main__':
    K = int(input())
    print(solve(K))
    if K <= 20:
        for s, e in path:
            print(f"{s} {e}")
