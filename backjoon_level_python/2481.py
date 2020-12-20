from collections import deque
import sys
input = sys.stdin.readline


def solve():
    # bfs
    parent = [-1] * N
    dq = deque()
    dq.append(0)
    parent[0] = 0
    while dq:
        v = dq.popleft()
        for e in adj[v]:
            if parent[e] == -1:
                dq.append(e)
                parent[e] = v

    # trace
    for j in Js:
        r = j-1
        if parent[r] == -1:
            print(-1)
            continue
        answer = ''
        while r:
            answer = str(r+1) + ' ' + answer
            r = parent[r]
        answer = '1' + ' ' + answer
        print(answer)


if __name__ == '__main__':
    # get input
    N, K = map(int, input().rstrip().split())
    binary_codes = list()
    binary_codes_dict = {}
    for k in range(N):
        input_text = input().rstrip()
        binary_codes.append(input_text)
        binary_codes_dict[input_text] = k
    M = int(input().rstrip())
    Js = [int(input().rstrip()) for _ in range(M)]

    # make adj
    adj = [[] for _ in range(N)]
    for idx, code in enumerate(binary_codes):
        for i, c in enumerate(code):
            temp_code = code[:i] + str(int(c)^1) + code[i+1:]
            if temp_code in binary_codes_dict:
                adj[idx].append(binary_codes_dict[temp_code])
    solve()