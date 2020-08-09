import sys
input = sys.stdin.readline

def mdist(dist, visited):
    min_dist = sys.maxsize
    min_idx = -1
    for i in range(1, len(dist)):
        if visited[i] is False and dist[i] < min_dist:
            min_idx = i
            min_dist = dist[i]
    return min_idx


def solve(n, edges, c):
    dist = [sys.maxsize for i in range(n+1)]
    visited = [False] * (n+1)
    v_num = 0

    dist[c] = 0

    for i in range(1, n+1):
        u = mdist(dist, visited) # 방문안한놈중 가장 거리 작은넘
        if u == -1:
            break
        visited[u] = True
        v_num += 1

        for v in edges[u]:
            if edges[u][v]+dist[u] < dist[v]:
                dist[v] = edges[u][v]+dist[u]
    # print(dist)

    time = -1
    for i in range(1, n+1):
        if dist[i] != sys.maxsize and time < dist[i]:
            time = dist[i]
    return '{} {}'.format(v_num, time)


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        n, d, c = map(int, input().split())
        edges = {i: dict() for i in range(1, n+1)}
        for j in range(d):
            a, b, s = map(int, input().split())
            edges[b][a] = s
        # print(edges) # d

        print(solve(n, edges, c))