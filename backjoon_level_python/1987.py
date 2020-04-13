# https://www.acmicpc.net/problem/1987
# pypy3
#144556KB	6768ms

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maximum = 1
history_alpha = [False] * 26


def dfs(depth, coordinate):
    global maximum

    x, y = coordinate

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if 0 <= temp_x < R and 0 <= temp_y < C and not visited[temp_x][temp_y] and history_alpha[ord(matrix[temp_x][temp_y])-ord('A')] is False:
            history_alpha[ord(matrix[temp_x][temp_y])-ord('A')] = True
            visited[temp_x][temp_y] = True
            maximum = max(depth + 1, maximum)
            dfs(depth+1, (temp_x, temp_y))
            visited[temp_x][temp_y] = False
            history_alpha[ord(matrix[temp_x][temp_y]) - ord('A')] = False


def solve():
    # history.append(matrix[0][0])
    history_alpha[ord(matrix[0][0])-ord('A')] = True
    visited[0][0] = True
    depth = 1

    dfs(depth, (0, 0))
    return maximum


if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [input() for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    # print(matrix)
    # print(visited)
    print(solve())
