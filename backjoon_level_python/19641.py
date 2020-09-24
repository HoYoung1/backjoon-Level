from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

count = 1


def solve(N, edges, root):
    visited = [False] * N
    copied_edges = deepcopy(edges)

    def dfs(node_num):
        global count

        edges[node_num]['left'] = count
        count += 1
        for n in sorted(map(int, copied_edges[node_num])):
            n = str(n)
            if visited[int(n)-1] is False:
                visited[int(n)-1] = True
                dfs(n)
        edges[node_num]['right'] = count
        count += 1
    visited[int(root)-1] = True
    dfs(root)

    return edges


if __name__ == '__main__':
    N = int(input().rstrip())
    edges = {}
    for i in range(N):
        info = input().rstrip().split()

        edges[info[0]] = {i: {} for i in info[1:-1]}

    root = input().rstrip()
    answer_edge = solve(N, edges, root)

    for i in range(1, N+1):
        key = str(i)
        print('{} {} {}'.format(key, answer_edge[key]['left'], answer_edge[key]['right']))

