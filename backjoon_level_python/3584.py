import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find_this_node_depth(u, depth):
    if parents[u] == u:
        return depth
    return find_this_node_depth(parents[u], depth+1)


def find_nth_parent(u, n):
    if n == 0:
        return u
    return find_nth_parent(parents[u], n-1)


def find_common_parent(u, v):
    if u == v:
        return u
    return find_common_parent(parents[u], parents[v])


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(input())  # 2 ≤ N ≤ 10,000

        # 입력 받기
        parents = [p for p in range(10001)]
        for j in range(N-1):
            A, B = map(int, input().split())
            parents[B] = A

        target1, target2 = map(int, input().split())
        t1_depth = find_this_node_depth(target1, 0)
        t2_depth = find_this_node_depth(target2, 0)
        # print(t1_depth)
        # print(t2_depth)

        if t1_depth > t2_depth:
            target1 = find_nth_parent(target1, t1_depth-t2_depth)
        elif t1_depth < t2_depth:
            target2 = find_nth_parent(target2, t2_depth-t1_depth)
        
        print(find_common_parent(target1, target2))





