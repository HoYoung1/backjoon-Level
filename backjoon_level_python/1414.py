def solve(N, matrix):
    parent = [i for i in range(N)]
    total_lan_length = 0
    connected_lan_length = 0
    connected_edge_num = 0
    edges = []
    # alpha to int
    for i in range(N):
        for j in range(N):
            if 'a' <= matrix[i][j] <= 'z':
                weight = ord(matrix[i][j]) - ord('a') + 1
            elif 'A' <= matrix[i][j] <= 'Z':
                weight = ord(matrix[i][j]) - ord('A') + 27
            elif matrix[i][j] == '0':
                weight = 0

            if weight != 0:
                total_lan_length += weight
                edges.append((i, j, weight))
    # print('total lan length', total_lan_length)

    edges.sort(key=lambda edge: edge[2])
    # print('edges', edges)

    # kruskal
    def find_parent(x):
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    for edge in edges:
        parent1 = find_parent(edge[0])
        parent2 = find_parent(edge[1])
        if parent1 != parent2: # 연결가능
            connected_edge_num += 1
            connected_lan_length += edge[2]
            # union
            if parent1 < parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
    if connected_edge_num != N-1:
        return -1
    return total_lan_length - connected_lan_length


if __name__ == '__main__':
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    print(solve(N, matrix))