from copy import deepcopy
import sys

A_list = []
B_list = []

input = sys.stdin.readline

def solve(N, C, weights):
    answer = 0
    A_set = weights[:N//2]
    B_set = weights[N//2:]

    def dfs(depth, group, n, subset, flag):
        d_subnet = deepcopy(subset)

        if flag:
            if group is A_set:
                A_list.append(d_subnet)
            elif group is B_set:
                B_list.append(d_subnet)

        if depth == n:
            return

        dfs(depth + 1, group, n, d_subnet + [group[depth]], True)
        dfs(depth + 1, group, n, d_subnet, False)

    dfs(0, A_set, len(A_set), list(), False)
    dfs(0, B_set, len(B_set), list(), False)
    print(A_list)
    print(B_list)
    return answer


def solve2(N, C, weights):
    answer = 0

    A_list = []
    B_list = []

    def dfs(start, end, s, group):
        if start >= end:
            group.append(s)
            return
        if s > C:
            return
        dfs(start + 1, end, s + weights[start], group)
        dfs(start + 1, end, s , group)

    dfs(0, N // 2, 0, A_list)
    dfs(N // 2 , N, 0, B_list)
    # print(A_list)
    # print(B_list)

    A_list.sort()
    B_list.sort()

    for A in A_list:
        for B in B_list:
            if A+B <= C:
                answer += 1
            else:
                break
    return answer


if __name__ == '__main__':
    N, C = map(int, input().split())
    weights = list(map(int, input().split()))

    print(solve2(N, C, weights))