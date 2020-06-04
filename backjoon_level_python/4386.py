import sys


# 답도없음. 다 연결되어있다는걸 보장하지않음
def solve(n, star_locations):
    answer = 0.0
    for i in range(n-1):
        minimum_cost = sys.maxsize
        for j in range(i+1, n):
            x, y = star_locations[i]
            x2, y2 = star_locations[j]
            minimum_cost = min(minimum_cost, round(((x2-x)**2 + (y2-y)**2)**0.5, 3))
        answer += minimum_cost
    return answer

# minimum_spanning_tree, kruskal
def solve2(n, star_locations):
    minimum_spanning_tree_cost = 0

    edges = sorted(make_edges(n, star_locations))
    edges.sort(key=lambda edge: edge[2])

    parent = list(range(n))

    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    for edge in edges:
        u, v, cost = edge
        parent_a = find_parent(u)
        parent_b = find_parent(v)
        if parent_a != parent_b: # 연결해도 사이클을 이루지 않으면
            minimum_spanning_tree_cost += cost
            parent[parent_a] = parent_b
    return minimum_spanning_tree_cost


def make_edges(n, star_locations):
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1, y1 = star_locations[i]
            x2, y2 = star_locations[j]
            cost = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
            edges.append((i, j, cost))
    return edges


if __name__ == '__main__':
    n = int(input())
    star_locations = []
    for _ in range(n):
        star_locations.append(list(map(float, input().split())))
    print(round(solve2(n, star_locations), 2))


