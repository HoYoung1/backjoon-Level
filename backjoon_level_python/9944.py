import sys
from enum import Enum
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


class MatrixState(Enum):
    LAND = 1
    WALL = 2
    VISITED = 3


def all_visited(board_map):
    for line in board_map:
        print(line)
    print()
    for line in board_map:
        if MatrixState.LAND in line:
            return False
    return True


def dfs(location):
    global move_count
    global min_move_count
    global visited

    x, y = location

    if all_visited(board_map):
        min_move_count = min(min_move_count, move_count)
        return

    for i in range(4):
        count_flag = False
        if 0 <= x + dx[i] < len(board_map) and 0 <= y + dy[i] < len(board_map[i]) and board_map[x + dx[i]][y + dy[i]] == MatrixState.LAND:
            while True:
                if 0 <= x + dx[i] < len(board_map) and 0 <= y + dy[i] < len(board_map[i]) and board_map[x + dx[i]][y + dy[i]] == MatrixState.LAND:
                    board_map[x][y] = MatrixState.VISITED  # 방문했다고 기록
                    x = x + dx[i]
                    y = y + dy[i]
                    count_flag = True
                else:
                    break
            if count_flag:
                move_count += 1
                board_map[x][y] = MatrixState.VISITED
                visited[x][y] = True
                dfs((x, y))
                visited[x][y] = False
                board_map[x][y] = MatrixState.LAND
                move_count -= 1


def solution(board_map):
    # 방문 리스트 초기화

    for i, line in enumerate(board_map):
        for j, s in enumerate(line):
            if s == MatrixState.LAND: # 갈 수 있는경우
                global_moving_count = 0
                dfs((i, j))
    return 0


if __name__ == '__main__':
    while True:
        move_count = 0
        min_move_count = sys.maxsize

        N, M = map(int, input().split())
        board_map = []
        case = 0
        # try:
        for i in range(N):
            line = input()
            temp_list = []
            for s in line:
                # 갈 수 있는 '.'은 0
                # 갈 수 없는 '*'은 1
                if s == '.':
                    temp_list.append(MatrixState.LAND)
                elif s == '*':
                    temp_list.append(MatrixState.WALL)
            board_map.append(temp_list)

        visited = []
        for i in board_map:
            temp_list = [False] * len(board_map[0])
            visited.append(temp_list)

        case += 1
        print("Case {}: {}".format(case, solution(board_map)))
        # except Exception as e:
        #     print(e)
        #     exit()


