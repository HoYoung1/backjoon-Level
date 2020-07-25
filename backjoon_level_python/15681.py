import sys
sys.setrecursionlimit(10**9)


def make_tree(current_node, parent):
    subtree_size = 1
    for v in linked[current_node]:
        if v != parent:
            subtree_size += make_tree(v, current_node)
    answer_queries[current_node] = subtree_size
    return subtree_size


if __name__ == '__main__':
    N, R, Q = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for i in range(N-1)]
    answer_queries = [0] * (N + 1)

    linked = [[] for _ in range(N+1)]

    for edge in edges:
        u, v = edge
        linked[u].append(v)
        linked[v].append(u)
    # print(linked)

    make_tree(R, -1)

    for _ in range(Q):
        query = int(sys.stdin.readline())
        print(answer_queries[query])




