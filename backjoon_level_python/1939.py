import sys
from collections import deque

maximum_weight = 0


def solve(N, M, infos, island_start, island_end):
    dq = deque()
    answer = 0

    def bfs(weight_limit):
        visited = [False] * (N + 1)
        global maximum_weight

        dq.append(island_start)
        visited[island_start] = True
        while dq:
            island = dq.popleft()
            for i in infos[island]:
                if not visited[i] and infos[island][i] >= weight_limit:
                    visited[i] = True
                    dq.append(i)

        if visited[island_end]:
            return True
        return False


    min_weight = 1
    max_weight = 1000000000

    while min_weight <= max_weight:
        mid = (min_weight + max_weight) // 2
        if bfs(mid):
            # 가능하면 더 높은 최대값 찾기
            answer = mid
            min_weight = mid + 1
        else:
            max_weight = mid - 1
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())

    # infos = [
    #     {
    #     },
    #     {
    #         2: 2,
    #         3: 3
    #     },
    #     {
    #         1: 2,
    #         3: 2
    #     },
    #     {
    #         1: 3,
    #         2: 2
    #     }
    # ]

    infos = [{} for _ in range(N+1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        if B in infos[A]:
            infos[A][B] = max(infos[A][B], C)
        else:
            infos[A][B] = C

        if A in infos[B]:
            infos[B][A] = max(infos[B][A], C)
        else:
            infos[B][A] = C

    island1, island2 = map(int, input().split())
    print(solve(N, M, infos, island1, island2))