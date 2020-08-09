from collections import deque


def topolopy_sort():
    # 진입차수가 0인놈 먼저 넣음
    for i in range(1, N + 1):
        if indgrees[i] == 0:
            dq.append(i)

    # 위상 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문
    for i in range(1, N + 1):
        # 만약 n개를 돌기전에 큐가 빈다면 사이클이 발생했다고 볼 수 있다.
        if not dq:
            return 0
        u = dq.popleft()
        answer.append(u)
        for v in edges[u]:
            indgrees[v] -= 1
            if indgrees[v] == 0:
                dq.append(v)
    return '\n'.join(map(str, answer))


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = {i: set() for i in range(N+1)} # init

    indgrees = [0] * (N+1)
    visited = [False] * (N+1)
    dq = deque()
    answer = []

    for i in range(M):
        singers = list(map(int, input().split()))[1:]
        for i in range(len(singers)-1):
            if singers[i+1] not in edges[singers[i]]:
                indgrees[singers[i+1]] += 1
            edges[singers[i]].add(singers[i+1])
    # print(edges)
    # print(indgrees)

    print(topolopy_sort())



