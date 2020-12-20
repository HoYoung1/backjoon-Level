from collections import deque


def check(code1, code2):
    count = 0
    for i in range(K):
        if code1[i] != code2[i]:
            count += 1
        if count >= 2:
            break

    return True if count == 1 else False


def solve():
    # make adj
    adj = [[False]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if check(binary_codes[i], binary_codes[j]):
                adj[i][j] = True
                adj[j][i] = True

    # for row in adj:
    #     print(row)
    # print()
    visited = [False] * N

    dq = deque()
    dq.append((A-1, str(A)))
    visited[A-1] = True
    while dq:
        v, path = dq.popleft()
        if v == B-1:
            return path
        for idx, is_connected in enumerate(adj[v]):
            new_path = path + ' ' + str(idx+1)
            if is_connected and visited[idx] is False:
                dq.append((idx, new_path))
                visited[idx] = True
    return -1


if __name__ == '__main__':
    N, K = map(int, input().split())
    binary_codes = [input() for _ in range(N)]
    A, B = map(int, input().split())

    print(solve())