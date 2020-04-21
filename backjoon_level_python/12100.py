# https://www.acmicpc.net/problem/12100
# 29380KB 780ms

from copy import deepcopy
maximum_value = 0

class Map2048:
    def __init__(self, N, mat):
        self.matrix = mat
        self.N = N

    def up(self):
        for j in range(self.N):
            current_std_x, current_std_y = -1, -1
            for i in range(self.N):
                if current_std_x != -1 and self.matrix[i][j] == self.matrix[current_std_x][current_std_y]:
                    self.matrix[current_std_x][current_std_y] *= 2
                    self.matrix[i][j] = 0
                    current_std_x, current_std_y = i, j
                elif self.matrix[i][j] != 0:
                    current_std_x, current_std_y = i, j

        # shift
        for j in range(self.N):
            num_zero = 0
            temp = []
            for i in range(self.N):
                if self.matrix[i][j] == 0:
                    num_zero += 1
                else:
                    temp.append(self.matrix[i][j])

            for i in range(self.N):
                if i < len(temp):
                    self.matrix[i][j] = temp[i]
                else:
                    self.matrix[i][j] = 0

    def down(self):
        for j in range(self.N-1, -1, -1):
            current_std_x, current_std_y = -1, -1
            for i in range(self.N-1, -1, -1):
                if current_std_x != -1 and self.matrix[i][j] == self.matrix[current_std_x][current_std_y]:
                    self.matrix[current_std_x][current_std_y] *= 2
                    self.matrix[i][j] = 0
                    current_std_x, current_std_y = i, j
                elif self.matrix[i][j] != 0:
                    current_std_x, current_std_y = i, j

        # shift
        for j in range(self.N):
            num_zero = 0
            temp = []
            for i in range(self.N):
                if self.matrix[i][j] == 0:
                    num_zero += 1
                else:
                    temp.append(self.matrix[i][j])

            for i in range(self.N):
                if i < self.N-len(temp):
                    self.matrix[i][j] = 0
                else:
                    self.matrix[i][j] = temp[i-(self.N-len(temp))]

    def left(self):
        for i in range(self.N):
            current_std_x, current_std_y = -1, -1
            for j in range(self.N):
                if current_std_x != -1 and self.matrix[i][j] == self.matrix[current_std_x][current_std_y]:
                    self.matrix[current_std_x][current_std_y] *= 2
                    self.matrix[i][j] = 0
                    current_std_x, current_std_y = i, j
                elif self.matrix[i][j] != 0:
                    current_std_x, current_std_y = i, j

        # shift
        for i in range(self.N):
            num_zero = 0
            temp = []
            for j in range(self.N):
                if self.matrix[i][j] == 0:
                    num_zero += 1
                else:
                    temp.append(self.matrix[i][j])
            self.matrix[i] = temp + [0] * num_zero


    def right(self):
        for i in range(self.N-1, -1, -1):
            current_std_x, current_std_y = -1, -1
            for j in range(self.N-1, -1, -1):
                if current_std_x != -1 and self.matrix[i][j] == self.matrix[current_std_x][current_std_y]:
                    self.matrix[current_std_x][current_std_y] *= 2
                    self.matrix[i][j] = 0
                    current_std_x, current_std_y = i, j
                elif self.matrix[i][j] != 0:
                    current_std_x, current_std_y = i, j

        # shift
        for i in range(self.N):
            num_zero = 0
            temp = []
            for j in range(self.N):
                if self.matrix[i][j] == 0:
                    num_zero += 1
                else:
                    temp.append(self.matrix[i][j])
            self.matrix[i] = [0] * num_zero + temp

    def get_max_value(self):
        result = 0
        for i in range(self.N):
            for j in range(self.N):
                result = max(result, self.matrix[i][j])
        return result

    # for debug
    def print_matrix(self):
        for row in self.matrix:
            for i in row:
                print('{:3}'.format(i), end="")
            print()
        print()


def dfs(depth, before_map, N):
    global maximum_value

    if depth == 5:
        maximum_value = max(maximum_value, before_map.get_max_value())
        return

    current_map = Map2048(N, deepcopy(before_map.matrix))
    current_map.up()
    dfs(depth + 1, current_map, N)

    current_map = Map2048(N, deepcopy(before_map.matrix))
    current_map.down()
    dfs(depth + 1, current_map, N)

    current_map = Map2048(N, deepcopy(before_map.matrix))
    current_map.left()
    dfs(depth + 1, current_map, N)

    current_map = Map2048(N, deepcopy(before_map.matrix))
    current_map.right()
    dfs(depth + 1, current_map, N)


def solve(N, matrix):
    map = Map2048(N, matrix)
    dfs(0, map, N)
    return maximum_value


if __name__ == '__main__':
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, matrix))
