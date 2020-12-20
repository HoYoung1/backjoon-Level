def solve(N, M):
    numbers = list(range(1, N+1))
    visited = [False] * N
    def dfs(depth, numbers, current):
        if depth == M:
            print(' '.join(map(str, current)))
            return
        for idx, number in enumerate(numbers):
            if visited[idx] is False:
                visited[idx] = True
                dfs(depth+1, numbers, current+[number])
                visited[idx] = False
    dfs(0, numbers, [])




if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)