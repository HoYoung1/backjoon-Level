# https://jaimemin.tistory.com/586
# 참고함

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


edges_count = None


def dfs(u, edges, visited):
    global edges_count

    v_count = 0
    for v in edges[u]:
        if visited[v] is False:
            visited[v] = True
            v_count += dfs(v, edges, visited)

    edges_count += len(edges[u])
    return v_count + 1


def get_sentence(trees_count):
    if trees_count == 0:
        msg = 'No trees.'
    elif trees_count == 1:
        msg = 'There is one tree.'
    else:
        msg = 'A forest of {} trees.'.format(trees_count)
    return msg


if __name__ == '__main__':
    while_count = 1

    while True:
        n, m = map(int, input().split()) # n ≤ 500과 m ≤ n(n-1)/2
        if n == 0 and m == 0:
            break

        visited = [False] * (n+1)

        edges_input = [map(int, input().split()) for i in range(m)]
        edges = [[] for _ in range(n + 1)]

        for edge in edges_input:
            u, v = edge
            edges[u].append(v)
            edges[v].append(u)
        # print(edges)

        trees_count = 0
        for i in range(1, n+1):
            if visited[i] is False:
                visited[i] = True
                edges_count = 0

                vertex_count = dfs(i, edges, visited)

                # print('현재 i : {} 현재 edges count {} '.format(i, edges_count))
                if vertex_count - 1 == (edges_count//2):
                    # print('vertex_count : {} , edges_count//2 : {} 트리입니다'.format(vertex_count ,edges_count//2))
                    trees_count += 1
                    print('tree count 가 더해짐 i: {}'.format(i))
        print('Case {}: {}'.format(while_count, get_sentence(trees_count)))
        while_count += 1







