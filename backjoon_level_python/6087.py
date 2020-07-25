import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
질문... 
False 로 했는데 안되서
숫자로변경하였다.
예를들어
3 3
C..
..C
... 
이 경우는 문제가없다 답은 1이다

허나
4 4
C...
o...
....
..C.
이경우 오른쪽아래를 출발이라고 가정,
정답은 (3,2) (3,1),(3,0),(2,0),(1,0),(0,0) 답은 1
만약 bfs순서상 (3,2), (2,2), (2,1), (2,0),(1,0),(0,0) 순으로 오면 답은 0이된다

풀다가 저런경우때문에 o표시한자리(1,0) 은 이미 방문처리가 되어서 초기값설정이안됫음..
  
"""

def solve():
    answer = sys.maxsize

    visited = [[[sys.maxsize] * 4 for _ in range(W)] for _ in range(H)]

    laser = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'C':
                laser.append((i, j))

    starting_point = laser.pop()
    x, y = starting_point
    # print('시작지점', x, y)

    dq = deque()
    for d in range(4):
        # dq.append((x, y, d, 0))
        visited[x][y][d] = 0

        next_x = x + dx[d]
        next_y = y + dy[d]
        next_d = d
        next_c = 0

        if 0 <= next_x < H and 0 <= next_y < W and visited[next_x][next_y][next_d] > next_c and matrix[next_x][
            next_y] != '*':
            dq.append((next_x, next_y, next_d, next_c))
            visited[next_x][next_y][next_d] = next_c
    while dq:
        x, y, d, c = dq.popleft()

        if x == laser[0][0] and y == laser[0][1]:
            # find answer
            answer = min(answer, c)
            # break

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_d = i
            next_c = c + 1 if i != d else c

            if 0 <= next_x < H and 0 <= next_y < W and visited[next_x][next_y][next_d] > next_c and matrix[next_x][
                next_y] != '*':
                dq.append((next_x, next_y, i, next_c))
                visited[next_x][next_y][next_d] = next_c

    return answer

# testcase
# 2 2
# .C
# C.
#
# 3 3
# ..C
# C..
# ...

if __name__ == '__main__':
    W, H = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]

    print(solve())
