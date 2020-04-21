# https://www.acmicpc.net/problem/15684
# 130004KB, 2932ms
# pypy3

import sys

minimum_num_bridge = sys.maxsize


# for debug
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


class GhostLeg:
    def __init__(self, matrix, bridges):
        self.matrix = matrix

        for i in range(len(bridges)):
            a, b = bridges[i]  # (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.
            a -= 1
            b -= 1

            self.matrix[a][b] = i+1
            self.matrix[a][b+1] = i+1
        # print_matrix(self.matrix)

    def trace_down(self, idx_col):
        for i in range(len(self.matrix)):
            if self.matrix[i][idx_col] == 0:
                continue
            elif self.matrix[i][idx_col] != 0:
                if 0 <= (idx_col-1) and self.matrix[i][idx_col-1] == self.matrix[i][idx_col]:
                    idx_col -= 1
                elif idx_col+1 < len(self.matrix[i]) and self.matrix[i][idx_col+1] == self.matrix[i][idx_col]:
                    idx_col += 1
        return idx_col


def dfs(depth, ghost_leg, N, H, start_i, start_j, visited):
    global minimum_num_bridge

    # print_matrix(ghost_leg.matrix)
    if is_i_to_i(N, ghost_leg):
        minimum_num_bridge = min(minimum_num_bridge, depth)
    if depth == 3:
        return

    for i in range(start_i, H):
        for j in range(start_j, N):
            start_j = 0
            if ghost_leg.matrix[i][j] == 0 and visited[i][j] is False:
                if j+1 < N and ghost_leg.matrix[i][j+1] == 0:
                    # can_put_bridge
                    ghost_leg.matrix[i][j] = chr(65 + depth) # for debug A B C
                    ghost_leg.matrix[i][j+1] = chr(65 + depth)  # for debug A B C
                    visited[i][j] = True

                    dfs(depth + 1, ghost_leg, N, H, i, j, visited)

                    visited[i][j] = False
                    ghost_leg.matrix[i][j] = 0
                    ghost_leg.matrix[i][j + 1] = 0


def solution(N, H, bridges):
    global minimum_num_bridge
    
    matrix = [[0]*N for _ in range(H)]
    visited = [[False]*N for _ in range(H)]

    ghost_leg = GhostLeg(matrix, bridges)

    # print(is_i_to_i(N, ghost_leg)) # 만약에 답 안나오면 이거 확인

    dfs(0, ghost_leg, N, H, 0, 0, visited)

    if minimum_num_bridge == sys.maxsize:
        minimum_num_bridge = -1
    return minimum_num_bridge


def is_i_to_i(N, ghost_leg):
    for i in range(N):
        result = ghost_leg.trace_down(i)
        if result != i:
            return False
    return True


if __name__ == '__main__':
    N, M, H = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]

    print(solution(N, H, bridges))




