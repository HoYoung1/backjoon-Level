import sys


class Sudoku:
    def __init__(self, matrix):
        self.matrix = matrix
        self.zeros = self._get_zeros()
        self.zeros_count = len(self.zeros)

    def run(self):
        depth = 0
        self._dfs(depth)

    def _dfs(self, depth):

        if depth == self.zeros_count:
            self.print_matrix()
            sys.exit()

        x, y = self.zeros[depth]

        for candidate in range(1, 10):
            # x, y 자리에 candidate 가 올 수 있는지 검사. 불가능하면 backtrack
            if self.promising(x, y, candidate):
                self.matrix[x][y] = candidate
                self._dfs(depth+1)
                self.matrix[x][y] = 0

    def _get_zeros(self):
        zeros = []
        for i, row in enumerate(self.matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        return zeros

    def print_matrix(self):
        for row in self.matrix:
            for i in row:
                print(i, end=" ")
            print()

    def promising(self, x, y, candidate):
        for i in range(9):
            # 행, 열을 검사하여 candidate 가 가능한 값인지 검사
            if self.matrix[x][i] == candidate or self.matrix[i][y] == candidate:
                return False

        # 같은 격자 내 candidate 가 가능한 값인지 검사
        start_row = x//3 * 3
        start_col = y//3 * 3
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if self.matrix[i][j] == candidate:
                    return False
        return True


if __name__ == '__main__':
    matrix = [list(map(int, input().split())) for _ in range(9)]
    sudoku = Sudoku(matrix)
    sudoku.run()

