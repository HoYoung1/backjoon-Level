# [링크와 스타트](https://www.acmicpc.net/problem/15661)
# 29284KB 3744ms

import sys


def dfs(depth, start_idx):
    global min_difference

    if depth == N//2:
        team_sum = 0
        for i in team:
            for j in team:
                team_sum += matrix[i][j]
        another_team_sum = 0
        for i in another_team:
            for j in another_team:
                another_team_sum += matrix[i][j]
        # print('t',team_sum)
        # print('k', another_team_sum)
        min_difference = min(min_difference, abs(team_sum-another_team_sum))
    else:
        for i in range(start_idx, N):
            team.append(i)
            another_team.remove(i)
            dfs(depth + 1, i+1)
            another_team.append(i)
            team.remove(i)


def solution(N):
    depth = 0
    start_idx = 0
    dfs(depth, start_idx)
    return min_difference


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    # print(matrix)
    team = []
    another_team = [i for i in range(N)]
    min_difference = sys.maxsize
    print(solution(N))