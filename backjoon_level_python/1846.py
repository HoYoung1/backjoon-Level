import sys
sys.setrecursionlimit(10**8)


def solve(N):
    forbidden_coordinates = []
    forbidden_col = []

    for i in range(N):
        forbidden_coordinates.append((i, i))
    for i in range(N):
        forbidden_coordinates.append((i, N - 1 - i))
    dfs(0, forbidden_coordinates, forbidden_col)
    return -1


def dfs(depth, f_coordinate, f_col):
    if depth == N:
        for num in f_col:
            print(num+1)
        sys.exit(0)

    for j in range(N):
        if (depth, j) in f_coordinate or j in f_col:
            continue

        f_col.append(j)
        dfs(depth + 1, f_coordinate, f_col)
        f_col.pop()


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
