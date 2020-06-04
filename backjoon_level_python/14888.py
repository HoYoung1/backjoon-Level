# https://www.acmicpc.net/problem/14888
# 29380KB 88ms

import sys

max_result = -sys.maxsize
min_result = sys.maxsize


def dfs(depth, current_value, add, sub, mul, div):
    global max_result, min_result
1
    if depth == N:
        max_result = max(max_result, current_value)
        min_result = min(min_result, current_value)
        return

    if add:
        next_value = current_value + A_list[depth]
        dfs(depth + 1, next_value, add-1, sub, mul, div)
    if sub:
        next_value = current_value - A_list[depth]
        dfs(depth + 1, next_value, add, sub-1, mul, div)
    if mul:
        next_value = current_value * A_list[depth]
        dfs(depth + 1, next_value, add, sub, mul-1, div)
    if div:
        # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
        if current_value < 0:
            next_value = int(current_value / A_list[depth])
        else:
            next_value = current_value // A_list[depth]
        dfs(depth + 1, next_value, add, sub, mul, div-1)


def solve():
    global max_result, min_result

    dfs(1, A_list[0], addition, subtraction, multiplication, division)
    return max_result, min_result


if __name__ == '__main__':
    N = int(input())
    A_list = list(map(int, input().split()))
    addition, subtraction, multiplication, division = map(int, input().split())

    max_result, min_result = solve()

    print(max_result)
    print(min_result)
