import sys

answer = sys.maxsize
def solve(N, M, X, edge_infos):
    global answer
    answer = 0
    memo = [(sys.maxsize, sys.maxsize) for _ in range(N + 1)]
    # 1 에서 N 으로 가는 가장 최적의 경로를 찾아야함
    # dp + dfs방식으로 해보자

    # edge 딕셔너리로 만들기
    edges = {i: [] for i in range(N + 1)}
    for edge in edge_infos:
        I, J, L, C = edge
        edges[I].append([J, L, C])
        edges[J].append([I, L, C])

    def dfs(vertex, time, capa):
        global answer
        for edge in edges[vertex]:
            u, l, c = edge
            min_capa = min(c, capa)
            current_weight = memo[u][0] + X//memo[u][1]
            new_weight = time + l + X//min_capa
            if u == N:
                answer = min(current_weight, new_weight)
            if current_weight > new_weight:
                memo[u] = (time+l, min_capa)
                dfs(u, time+l, min_capa)
    memo[1] = (-1, -1)
    dfs(1, 0, sys.maxsize)
    return answer


if __name__ == '__main__':
    N, M, X = map(int, input().split())

    edge_infos = [list(map(int, input().split())) for i in range(M)]
    print(solve(N, M, X, edge_infos))
