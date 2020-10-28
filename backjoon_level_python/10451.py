import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def solve(N, edges):
    result = 0
    visited = [0] * (N+1)
    def dfs(u):
        # -1 은 아직 돌고 있는데 들어왔다는것 즉 사이클이 있음
        # 1 은 끝났다는 의미
        if visited[u] == -1:
            return True
        elif visited[u] == 1:
            return False

        visited[u] = -1
        if dfs(edges[u]):
            visited[u] = 1
            return True
        visited[u] = 1
        return False

    for i in range(1, N+1):
        if dfs(i):
            result += 1
    return result


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input().rstrip()    )
        numbers = list(map(int, input().rstrip().split()))
        edges = {idx+1: number for idx, number in enumerate(numbers)}
        print(solve(N, edges))


