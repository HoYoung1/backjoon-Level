import sys
input = sys.stdin.readline


def get_first_stone_num(stones, connection_flags):
    temp = sys.maxsize
    for idx, flag in enumerate(connection_flags):
        temp = min(temp, stones[idx])
        if flag is False:
            return temp
    return temp


if __name__ == '__main__':
    N, M, K = map(int, input().rstrip().split())
    stones = list(map(int, input().rstrip().split()))
    disconnection = [list(map(int, input().rstrip().split())) for i in range(M)]

    connection_flags = [True] * N
    for d in disconnection:
        i, j = d
        if (i, j) in [(1, N), (N, 1)]:
            connection_flags[-1] = False
        else:
            min_num = min(i, j)
            connection_flags[min_num - 1] = False
    # print(connection_flags)

    temp = sys.maxsize
    flag_count = 0
    for idx, flag in enumerate(connection_flags):
        temp = min(temp, stones[idx])
        if flag is False:
            K -= temp
            temp = sys.maxsize
        flag_count += 1

    if connection_flags[-1] is True:
        first_num = get_first_stone_num(stones, connection_flags)
        if first_num > temp:
            K -= first_num-temp

    # print('K', K)
    # print(K)
    if K >= 0 or M <= 1:
        print('YES')
    else:
        print('NO')


