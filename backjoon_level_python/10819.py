# 10819  https://www.acmicpc.net/problem/10819
# 차이를 최대로
maximum_value = 0 # init
current_value = 0


def dfs(depth, before_value):
    global maximum_value
    global current_value

    if depth == N:
        maximum_value = max(maximum_value, current_value)
        return

    for idx, value in enumerate(A):
        if not visited[idx]:
            current_value += abs(before_value - value)
            visited[idx] = True
            dfs(depth+1, value)
            visited[idx] = False
            current_value -= abs(before_value - value)


def solve():
    depth = 1
    for idx, value in enumerate(A):
        visited[idx] = True
        dfs(depth, value)
        visited[idx] = False
    return maximum_value


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    visited = [False for _ in range(len(A))]
    print(solve())