# https://www.acmicpc.net/problem/15658
# 29380KB 284ms
import sys

maximum = -sys.maxsize
minimum = sys.maxsize


def solve(numbers, add, sub, mul, div):
    def dfs(depth, current_value):
        global add, sub, mul, div
        global maximum, minimum
        if depth == N-1:
            maximum = max(maximum, current_value)
            minimum = min(minimum, current_value)
            return
        if add:
            add -= 1
            dfs(depth + 1, current_value + numbers[depth + 1])
            add += 1
        if sub:
            sub -= 1
            dfs(depth + 1, current_value - numbers[depth + 1])
            sub += 1
        if mul:
            mul -= 1
            dfs(depth + 1, current_value * numbers[depth + 1])
            mul += 1
        if div:
            div -= 1
            dfs(depth + 1, int(current_value / numbers[depth + 1]))
            div += 1

    dfs(0, numbers[0])
    return maximum, minimum


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    for answer in solve(numbers, add, sub, mul, div):
        print(answer)