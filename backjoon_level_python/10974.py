def dfs(depth):
    if depth == N:
        for num in permutation:
            print(num, end=" ")
        print()
        return

    for idx, number in enumerate(numbers):
        if not visited[idx]:
            visited[idx] = True
            permutation.append(number)
            dfs(depth+1)
            permutation.remove(number)
            visited[idx] = False

def solve(N):
    depth = 0
    dfs(depth)


if __name__ == '__main__':
    N = int(input())
    numbers = [i for i in range(1, N+1)]
    visited = [False for i in range(1, N+1)]
    permutation = []
    solve(N)