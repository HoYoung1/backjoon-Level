def dfs(depth, current):
    if depth == M:
        print(' '.join(map(str, current)))
        return

    for number in numbers:
        dfs(depth + 1, current + [number])


def solve():
    dfs(0, [])


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    solve()