import sys


def solve(N, matrix):
    VISITED_ALL = (1 << N) - 1
    memo = [[None] * (1 << N) for _ in range(N)]

    def dfs(current, visited):
        if visited == VISITED_ALL:
            return matrix[current][0] or sys.maxsize
        if memo[current][visited] is not None:
            return memo[current][visited]

        tmp = sys.maxsize
        for i in range(N):
            if matrix[current][i] != 0 and visited & (1 << i) == 0:
                tmp = min(tmp, dfs(i, visited | (1 << i)) + matrix[current][i])
        memo[current][visited] = tmp
        return memo[current][visited]

    answer = dfs(0, 1<<0)
    return answer


if __name__ == '__main__':
    N = int(input())# city num
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, matrix))