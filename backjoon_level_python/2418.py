# 다른 사람 풀이도 보기!!

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 이차원배열로했는데 아님~ 3차원필요해서 solve2로 넘어감
def solve():
    dp = [[-1] * W for _ in range(H)]
    answer = 0

    def find(depth, i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        if depth == L - 1:
            dp[i][j] = 1
            return 11

        dp[i][j] = 0

        for k in range(8):
            next_x = i + dx[k]
            next_y = j + dy[k]
            if 0 <= next_x < H and 0 <= next_y < W and matrix[next_x][next_y] == word[depth + 1]:
                dp[i][j] += find(depth + 1, next_x, next_y)
        return dp[i][j]

    for i in range(H):
        for j in range(W):
            if matrix[i][j] == word[0]:
                answer += find(0, i, j)
    return answer


def solve2():
    dp = [[[-1] * L for _ in range(W)] for _ in range(H)]
    answer = 0

    def find(depth, i, j):
        if dp[i][j][depth] != -1:
            return dp[i][j][depth]

        if depth == L - 1:
            dp[i][j][depth] = 1
            return dp[i][j][depth]

        dp[i][j][depth] = 0

        for k in range(8):
            next_x = i + dx[k]
            next_y = j + dy[k]
            if 0 <= next_x < H and 0 <= next_y < W and matrix[next_x][next_y] == word[depth + 1]:
                # print(next_x,next_y)
                dp[i][j][depth] += find(depth + 1, next_x, next_y)
        return dp[i][j][depth]

    for i in range(H):
        for j in range(W):
            if matrix[i][j] == word[0]:
                answer += find(0, i, j)
    return answer

if __name__ == '__main__':
    H, W, L = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    word = input()

    print(solve2())
