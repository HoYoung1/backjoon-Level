def solve():
    dfs(0, [])


def dfs(depth, current):
    if depth == M:
        print(' '.join(map(str, current)))
        return
    for idx, number in enumerate(numbers):
        if visited[idx] is False:
            visited[idx] = True
            dfs(depth+1, current + [number])
            visited[idx] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    visited = [False] * len(numbers)
    solve()