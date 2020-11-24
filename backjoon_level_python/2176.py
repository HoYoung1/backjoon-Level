import sys
import heapq

def solve(N, M, matrix):
    # make adj
    adj = {i: [] for i in range(N+1)}
    dist = [sys.maxsize] * (N+1)
    dp = [0] * (N+1)
    for row in matrix:
        u, v, distance = row
        adj[u].append((distance, v))
        adj[v].append((distance, u))

    hq = []
    start = 2
    dp[start] = 1
    dist[start] = 0
    heapq.heappush(hq, (0, 2))

    while hq:
        current_distance, vertex = heapq.heappop(hq)

        for distance, u in adj[vertex]:
            next_dis = distance + current_distance
            if next_dis < dist[u]:
                dist[u] = next_dis
                heapq.heappush(hq, (dist[u], u))
            # 아래 if문이 핵심!!
            if dist[u] < current_distance:
                dp[vertex] += dp[u]
    return dp[1]


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split()))for _ in range(M)]
    print(solve(N, M, matrix))