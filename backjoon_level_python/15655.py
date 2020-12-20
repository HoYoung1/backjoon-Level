def dfs(depth, current, start):
    if depth == M:
        print(' '.join(map(str, current)))
        return

    for idx, number in enumerate(numbers[start:]):
        dfs(depth + 1, current + [number], start+idx+1)


def solve():
    dfs(0, [], 0)


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    solve()