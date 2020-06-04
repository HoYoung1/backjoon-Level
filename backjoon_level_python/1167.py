from collections import deque


def solve(V, edges):
    def bfs(start: int) -> int:
        farthest_idx = 0

        weights = [0] * (V + 1)
        weights[start] = 0

        dq = deque()
        dq.append(start)

        while dq:
            idx = dq.popleft()
            for v in edges[idx]:
                if weights[v] == 0 and v != start:
                    weights[v] = edges[idx][v] + weights[idx]
                    dq.append(v)

                    if weights[v] > weights[farthest_idx]:
                        farthest_idx = v
        return farthest_idx, weights

    farthest_u, _ = bfs(1)
    _, distances = bfs(farthest_u)
    return max(distances)


if __name__ == '__main__':
    V = int(input())
    edges = [{} for _ in range(V+1)]
    for _ in range(V):
        edge_info = list(map(int, input().split()))
        for i in range(1, len(edge_info)-1, 2):
            u = edge_info[0]
            v = edge_info[i]
            weight = edge_info[i+1]
            edges[u][v] = weight
    # print(edges)

    print(solve(V, edges))
