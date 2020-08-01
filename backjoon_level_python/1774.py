def get_parent(x):
    if x == parents[x]:
        return x
    return get_parent(parents[x])


def solve(N, M, locations, existing_edges):
    answer = 0

    # 이미 연결된 엣지 부모 표시
    for edge in existing_edges:
        u, v = edge
        p1 = get_parent(u)
        p2 = get_parent(v)
        if p1 != p2:
            if p1 > p2:
                parents[p1] = p2
            else:
                parents[p2] = p1

    # 모든 간선을 구하자
    edges = []
    for u in range(1, N+1):
        for v in range(u+1, N+1):
            x1, y1 = locations[u]
            x2, y2 = locations[v]
            distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
            edges.append((u, v, distance))

    edges.sort(key=lambda edge:edge[2])

    current_edge_num = len(existing_edges)

    for edge in edges:
        if N - 1 == current_edge_num:
            break

        u, v, distance = edge

        p1 = get_parent(u)
        p2 = get_parent(v)
        if p1 != p2:
            if p1 > p2:
                parents[p1] = p2
            else:
                parents[p2] = p1
            # parents[p1] = p2
            answer += distance
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    locations = [0] + [list(map(int, input().split())) for i in range(N)]
    existing_edges = [list(map(int, input().split())) for i in range(M)]

    parents = [i for i in range(0, N + 1)]

    print('{:.2f}'.format(solve(N, M, locations, existing_edges)))