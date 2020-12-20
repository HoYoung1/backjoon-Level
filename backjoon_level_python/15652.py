def solve():
    dfs(0, [], 0)


def dfs(depth, current, start):
    if depth == M:
        print(' '.join(map(str, current)))
        return
    for idx, number in enumerate(numbers[start:]):
        dfs(depth+1, current + [number], idx + start)


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(range(1, N+1))
    solve()