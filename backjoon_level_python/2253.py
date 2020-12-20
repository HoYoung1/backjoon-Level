import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def jump(idx, len):
    global success

    if idx == N:
        success = True
        return 0

    result = cache[idx][len]
    if result != -1:
        return result

    result = sys.maxsize
    for i in [-1, 0, 1]:
        # ㄷㅏ음 속도가 1이상이고
        if len + i >= 1:
            next = idx + (len + i)
            # 범위 내에 있는 돌이고 갈 수 있는 돌일 때만 재귀 함수 호출
            if next <= N and not rock[next]:
                result = min(result, 1 + jump(next, (len + i)))

    return result


def solve3(N, M, small_stones):
    global success

    result = jump(1, 0)
    if success:
        return result
    else:
        return -1


def dp(pos, jump):
    # 기저
    if pos >= N:
        return -1
    if pos == N-1:
        return 1
    if check



if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    small_stones = [int(input().rstrip()) for _ in range(M)]

    MAX = 10001
    # cache = [[-1] * 250 for _ in range(MAX)]
    check = [False] * MAX

    for small_stone in small_stones:
        check[small_stone-1] = True

    print(dp(1,1))