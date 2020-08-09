import sys
from copy import deepcopy

def next_permutation(current_list):
    # list[i] < list[i+1] 만족하는 가장 마지막 i를 찾는다.
    last_i = None
    for i in range(len(current_list)-1):
        if current_list[i] < current_list[i+1]:
            last_i = i

    # find j
    #
    last_j = None
    for j in range(last_i, len(current_list)):
        if current_list[last_i] < current_list[j]:
            last_j = j

    # 만약에 last_j 를 못찾으면, 이미 그 순열이 가장 마지막 순열이다.
    # print(last_i, last_j)
    # swap i, j
    current_list[last_i], current_list[last_j] = current_list[last_j], current_list[last_i]

    current_list[last_i+1:] = reversed(current_list[last_i+1:])

    # print(current_list)
    return current_list

def solve(N, F):
    # dfs(0, [])
    if N == 1:
        print(1)
        return
    current_list = [i for i in range(1, N+1)]

    while True:
        if get_tree_sum(current_list) == F:
            break
        current_list = next_permutation(current_list)
    print(' '.join(map(str, current_list)))

    return


def get_tree_sum(current_list):
    tmp_list = deepcopy(current_list)
    while len(tmp_list) != 1:
        tmp_tmp_list = []

        for i in range(len(tmp_list)-1):
            tmp_tmp_list.append(tmp_list[i] + tmp_list[i+1])
        tmp_list = tmp_tmp_list
    return tmp_list[0]



def dfs(depth, current_list):

    if depth == N:
        # print(current_list)
        tree_sum = get_tree_sum(current_list)
        # print('tree_sum', tree_sum)
        if tree_sum == F:
            print(' '.join(map(str, current_list)))
            sys.exit(0)

    for i in range(1, N+1):
        if visited[i] is False:
            current_list.append(i)
            visited[i] = True
            dfs(depth+1, current_list)
            visited[i] = False
            current_list.pop()


if __name__ == '__main__':
    N, F = map(int, input().split())
    visited = [False] * (N+1)
    solve(N, F)