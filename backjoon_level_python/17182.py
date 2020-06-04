import sys
from copy import deepcopy

result = sys.maxsize

# 완적탐색 시간초과 ㅠ.ㅠ
def solve(N, K, visited_path, matrix):

    def dfs(current_idx, current_point, current_visited_palnets):
        global result

        current_visited_palnets[current_idx] = True
        if False not in current_visited_palnets:
            result = min(result, current_point)
            return
        for i in range(N):
            if current_idx != i and not visited_path[current_idx][i]:
                # 돌아갈 조건이 전혀 필요없으면

                visited_path[current_idx][i] = True
                dfs(i, current_point + matrix[current_idx][i], deepcopy(current_visited_palnets))
                visited_path[current_idx][i] = False

    dfs(K, 0, [False]*N)
    return result


def solve2(N, K, visited_path, matrix):
    dp = deepcopy(matrix)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


    def dfs(depth, current_value, current_idx):
        global result

        if depth == N-1:
            result = min(result, current_value)
            return

        for i in range(N):
            if not current_visited[i]:
                current_visited[i] = True
                dfs(depth + 1, current_value + dp[current_idx][i], i)
                current_visited[i] = False

    current_visited[K] = True
    dfs(0, 0, K)
    return result


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    visited_path = [[False] * N for _ in range(N)]
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    current_visited = [False] * N

    print(solve2(N, K, visited_path, matrix))
