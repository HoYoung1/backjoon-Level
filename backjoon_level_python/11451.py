from collections import deque
from enum import Enum

dx = [-1,1,0,0]
dy = [0,0,-1,1]

class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    WEST = 'W'
    EAST = 'E'

class PacMan:
    def __init__(self, m, n, map):
        self.m = m
        self.n = n
        self.map = map
        self.p1, self.p2 = self._get_pacman_loactions()
        self.avaiable_list = []
        # print(self.p1, self.p2)

    def _get_pacman_loactions(self):
        result = []
        for i in range(self.m):
            for j in range(self.n):
                if self.map[i][j] == 'P':
                    result.append((i,j))
        return result

    def start(self):
        dq = deque()
        p1_x, p1_y = self.p1
        p2_x, p2_y = self.p2
        for i in range(4):
            if self.map[(p1_x + dx[i]) % self.m][(p1_y + dy[i]) % self.n] == 'G' or self.map[(p2_x + dx[i]) % self.m][(p2_y+dy[i]) % self.n] == 'G':
                continue
            elif self.map[(p1_x + dx[i]) % self.m][(p1_y + dy[i]) % self.n] == 'X' and self.map[(p2_x + dx[i]) % self.m][(p2_y + dy[i]) % self.n] == 'X':
                continue
            dq.append(((p1_x + dx[i], p1_y + dy[i]), (p2_x + dx[i], p2_y+dy[i]), ''+list(Direction)[i].value))
        while dq:
            p1_loc, p2_loc, path = dq.popleft()
            if p1_loc == p2_loc:
                self.avaiable_list.append(path)
            else:



if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())
        matrix = [input() for _ in range(M)]
        pac_man = PacMan(M, N, matrix)
        pac_man.start()