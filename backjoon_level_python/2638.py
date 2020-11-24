from enum import Enum
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class LandType(Enum):
    AIR_OUTSIDE = 2
    CHEESE = 1
    AIR_INSIDE = 0


def bfs(matrix, exposure_matrix, xx, yy):
    if matrix[xx][yy] == LandType.AIR_OUTSIDE.value:
        return []

    next_cheeses = []

    dq = deque()
    dq.append((xx, yy))
    matrix[xx][yy] = LandType.AIR_OUTSIDE.value
    for i in range(4):
        nxx = xx + dx[i]
        nyy = yy + dy[i]
        if 0 <= nxx < N and 0 <= nyy < M and matrix[nxx][nyy] == LandType.CHEESE.value:
            exposure_matrix[nxx][nyy] += 1
            if exposure_matrix[nxx][nyy] == 2:
                next_cheeses.append((nxx, nyy))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == LandType.AIR_INSIDE.value:
                matrix[nx][ny] = LandType.AIR_OUTSIDE.value
                dq.append((nx, ny))
                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]
                    if 0 <= nnx < N and 0 <= nny < M and matrix[nnx][nny] == LandType.CHEESE.value:
                        exposure_matrix[nnx][nny] += 1
                        if exposure_matrix[nnx][nny] == 2:
                            next_cheeses.append((nnx, nny))
    return next_cheeses


def solve(N, M, matrix):
    exposure_matrix = [[0] * M for _ in range(N)]

    # 11시 1시 5시 7시 방향에서 bfs 시작
    cheeses = []
    cheeses += bfs(matrix, exposure_matrix, 0, 0)
    cheeses += bfs(matrix, exposure_matrix, N - 1, 0)
    cheeses += bfs(matrix, exposure_matrix, 0, M - 1)
    cheeses += bfs(matrix, exposure_matrix, N - 1, M - 1)

    next_cheeses = []
    answer = 0
    while True:
        answer += 1

        for x, y in cheeses:
            matrix[x][y] = -1  # finish
            next_cheeses += bfs(matrix, exposure_matrix, x, y)
        if next_cheeses:
            cheeses = next_cheeses
            next_cheeses = []
        else:
            break
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, M, matrix))


import json
import boto3

secrets = boto3.client("secretsmanager")
rds = json.dumps(secrets.get_secrets_value("prod/TwitterApp/Database")['SecretString'])

print(rds)
# 그러면 다음과 같은 값이 나옵니다.
"""
{
    'engine': 'mysql',
    'host': 'twitterapp2.abcdefg.us-east-1.rds.amazonaws.com',
    'password': '-)Kw>THISISAFAKEPASSWORD:lg{&sad+Canr',
    'port': 3306,
    'username': 'ranman'
}
"""

