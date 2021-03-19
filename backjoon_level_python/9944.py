# all visit 갯수로
# 백트래킹 조건 넣은 것
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(depth, x, y):
    global answer, visited_cnt

    if depth > answer:  # 이 백트래킹 조건이 들어가야 시간 단축이 좋을 듯,
        return

    if all_visited(visited_cnt):
        answer = min(answer, depth)
        return

    for k in range(4):
        next_x, next_y = x + dx[k], y + dy[k]
        temp_q = []
        while 0 <= next_x < N and 0 <= next_y < M and visited[next_x][next_y] is False and matrix[next_x][
            next_y] == '.':
            # dash
            visited_cnt += 1
            visited[next_x][next_y] = True
            temp_q.append((next_x, next_y))
            next_x, next_y = next_x + dx[k], next_y + dy[k]
        if temp_q:
            next_x, next_y = next_x - dx[k], next_y - dy[k]
            dfs(depth + 1, next_x, next_y)
            # visit 원복
            for q_x, q_y in temp_q:
                visited_cnt -= 1
                visited[q_x][q_y] = False


def all_visited(cnt):
    return all_cnt == cnt


def solve():
    global visited_cnt

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.':
                visited_cnt = 1

                visited[i][j] = True
                dfs(0, i, j)
                visited[i][j] = False
    return answer if answer != sys.maxsize else -1


def get_all_cnt():
    result = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.':
                result += 1
    return result


if __name__ == '__main__':
    try:
        loop_cnt = 1
        while True:
            answer = sys.maxsize
            N, M = map(int, input().rstrip().split())
            matrix = [input().rstrip() for _ in range(N)]

            all_cnt = get_all_cnt()
            visited_cnt = 0
            visited = [[False] * M for _ in range(N)]
            print(f'Case {loop_cnt}: {solve()}')
            loop_cnt += 1
    except:
        exit()
