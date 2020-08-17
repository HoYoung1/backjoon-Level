# 가장 path가 긴거를 2배 시키면 되는가?
import sys


def min_distance_node(path, N, visited):
    min_idx = sys.maxsize
    min_value = sys.maxsize
    for i in range(1, N+1):
        if visited[i] is False and path[i][0] < min_value :
            min_idx = i
            min_value = path[i][0]
    return min_idx


def dijkstra(source):
    path = [[sys.maxsize, None]] * (N+1)
    visited = [False] * (N+1)

    path[source] = [0, source]
    for i in range(1, N):
        u = min_distance_node(path, N, visited)
        # print(u)
        visited[u] = True
        
        for v in range(1, N+1):
            if visited[v] is False and v in edges[u] and path[u][0] + edges[u][v] < path[v][0]:
                path[v] = [path[u][0] + edges[u][v], u]
    # print(visited)
    # print(path)

    return path


def get_longest_way(min_distances, N):
    current_max_distance = -1
    current_node = N
    while True:
        distance, before_node = min_distances[current_node]
        if distance == 0 and before_node == 1:
            break
        if current_max_distance < edges[before_node][current_node]:
            current_max_distance = edges[before_node][current_node]
            u, v = before_node, current_node

        current_node = before_node
    return u, v


if __name__ == '__main__':
    N, M = map(int, input().split())
    # 인접 리스트로 변경하자
    # edges = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
    edges = {i:{} for i in range(1,N+1)}

    for i in range(M):
        A, B, L = map(int, input().split())
        edges[A][B] = L
        edges[B][A] = L
    # print(edges)

    min_distances = dijkstra(1)

    # u, v = get_longest_way(min_distances, N)
    # 하나씩 두배로 늘려보고 다시 다익스트라 돌려봄
    u, v = min_distances[N][1], N
    max_distance = 0
    while True:
        # print('u, v',u,v, edges[u][v])
        edges[u][v] = edges[u][v] * 2
        edges[v][u] = edges[v][u] * 2

        temp_path = dijkstra(1) # return 받기
        max_distance = max(max_distance, temp_path[N][0])
        # print(max_distance)
        if u == 1:
            break

        edges[u][v] = edges[u][v] // 2
        edges[v][u] = edges[v][u] // 2
        u, v = min_distances[u][1], u

    # print(edges)

    min_distances_after_interfering = dijkstra(1)
    print(max_distance - min_distances[N][0])





