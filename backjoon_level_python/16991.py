import sys


def get_distance(city1, city2):
    return ((matrix[city2][0] - matrix[city1][0]) ** 2 + (matrix[city2][1] - matrix[city1][1]) ** 2) ** 0.5


def solve(N, matrix):
    VISITED_ALL = (1 << N) - 1
    memo = [[None] * (1 << N) for _ in range(N)]

    def dfs(current, visited):
        if visited == VISITED_ALL:
            # return matrix[current][0] or sys.maxsize
            return get_distance(current, 0)
        if memo[current][visited] is not None:
            return memo[current][visited]

        tmp = sys.maxsize
        for i in range(N):
            if visited & (1 << i) == 0:
                # tmp = min(tmp, dfs(i, visited | (1 << i)) + matrix[current][i])
                tmp = min(tmp, dfs(i, visited | (1 << i)) + get_distance(current,i))
        memo[current][visited] = tmp
        return memo[current][visited]

    answer = dfs(0, 1<<0)
    return answer


if __name__ == '__main__':
    N = int(input()) # city num
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, matrix))