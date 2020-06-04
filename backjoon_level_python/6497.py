def get_parent(table, x):
    if x == table[x]:
        return x
    return get_parent(table, table[x])


def union(n1_parent, n2_parent):
    if n1_parent < n2_parent:
        parent_table[n2_parent] = n1_parent
    else:
        parent_table[n1_parent] = n2_parent


if __name__ == '__main__':
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        edges = [input().split() for _ in range(n)]

        parent_table = [i for i in range(200000)]

        edges.sort(key=lambda edge: int(edge[2]))
        total_cost = sum([int(edge[2]) for edge in edges])
        # print(edges)
        minimum_spanning_cost = 0

        for edge in edges:
            n1, n2, distance = map(int, edge)
            n1_parent = get_parent(parent_table, n1)
            n2_parent = get_parent(parent_table, n2)
            if n1_parent != n2_parent:
                minimum_spanning_cost += distance
                union(n1_parent, n2_parent)
        print(total_cost - minimum_spanning_cost)







    