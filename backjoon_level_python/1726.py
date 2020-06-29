# 32280KB 104ms

# 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
from enum import Enum
from collections import deque

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# Original Direction
class Direction(Enum):
    EAST = 1
    WEST = 2
    SOUTH = 3
    NORTH = 4

def bfs4():

    dq = deque()
    dq.append((start_x, start_y, start_direction, 0))
    visited[start_x][start_y][start_direction] = True
    while dq:
        x, y, d, order_count = dq.popleft()
        if x == end_x and y == end_y and d == end_direction:
            return order_count

        for j in range(1, 4):
            next_x = x + dx[d] * j
            next_y = y + dy[d] * j
            if 1 <= next_x <= M and 1 <= next_y <= N and not visited[next_x][next_y][d]:
                if matrix[next_x][next_y] == 1: # 못감
                    break
                dq.append((next_x, next_y, d, order_count + 1))
                visited[next_x][next_y][d] = True

        # Turn left or Turn right
        d += 1
        d %= 4
        if not visited[x][y][d]:
            dq.append((x, y, d, order_count + 1))
            visited[x][y][d] = True

        # Turn left or Turn right
        d -= 2
        d %= 4

        if not visited[x][y][d]:
            dq.append((x, y, d, order_count + 1))
            visited[x][y][d] = True

        # Turn back
        d -= 1
        d %= 4

        if not visited[x][y][d]:
            dq.append((x, y, d, order_count + 2))
            visited[x][y][d] = True


if __name__ == '__main__':
    # 첫째 줄에 공장 내 궤도 설치 상태를 나타내는 직사각형의 세로 길이 M과 가로 길이 N
    M, N = map(int, input().split())  # 둘 다 100이하의 자연수이다.
    matrix = [[0]] + [[0] + list(map(int, input().split())) for _ in range(M)]
    visited = [[0]] + [[0] + [False] * N for _ in range(M)]
    for i in range(1,M+1):
        for j in range(1, N+1):
            visited[i][j] = [False]*4
    start_x, start_y, start_direction = map(int, input().split())  # 로봇의 출발 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다
    # print(start_x)
    end_x, end_y, end_direction = map(int, input().split())

    # 남쪽과 서쪽을 바꿔서 코딩해야 편함.
    if start_direction == 2:
        start_direction = 3
    elif start_direction == 3:
        start_direction = 2
    if end_direction == 2:
        end_direction = 3
    elif end_direction == 3:
        end_direction = 2

    start_direction -= 1
    end_direction -= 1

    answer = bfs4()
    print(answer)
