# 트리의 지름? 문제인것같기도하고..
from collections import deque


def solve():
    if edges == {}:
        return 0
    def bfs(u):
        visited = [False] * (len(edges)+1)
        max_vertex = u
        max_distance = 0

        dq = deque()
        dq.append((u, 0))
        visited[u] = True
        while dq:
            vertex, current_distance = dq.popleft()
            if current_distance > max_distance:
                max_distance = current_distance
                max_vertex = vertex
            for target in edges[vertex]:
                if visited[target] is False:
                    visited[target] = True
                    dq.append((target, current_distance + edges[vertex][target]))
        return max_vertex, max_distance
    v, _ = bfs(1)
    _, max_distance = bfs(v)
    return max_distance

if __name__ == '__main__':
    edges = {}
    while True:
        try:
            u, v, distance = list(map(int, input().split()))

            if u in edges:
                edges[u][v] = distance
            else:
                edges[u] = {
                    v: distance
                }
            if v in edges:
                edges[v][u] = distance
            else:
                edges[v] = {
                    u: distance
                }
        except:
            break
    print(solve())