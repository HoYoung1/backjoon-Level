import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve(N, X, Y):
    dp = [[-1] * 1001 for _ in range(1001)]

    dp[0][0] = (X[0] - Y[0]) ** 2

    def find(i, j):
        if i < 0 or j < 0:
            return sys.maxsize
        if dp[i][j] != -1:
            return dp[i][j]

        min_num = sys.maxsize
        for dx, dy in [[-1,0], [0, -1], [-1, -1]]:
            if i + dx >= 0 and j + dy >= 0:
                min_num = min(min_num, find(i+dx, j+dy))
        # print('min1 : {} , min2 : {} , min3 : {}'.format(min1, min2, min3))

        dp[i][j] = (X[i] - Y[j]) ** 2 + min_num
        return dp[i][j]

    return find(N-1, N-1)


if __name__ == '__main__':
    N = int(input()) # 입력a의 첫 줄에는 파형의 길이를 나타내는 자연수 N
    X = list(map(int, input().split()))  # 두 번째 줄에는 첫 파형 X의 시간 별 높이를 나타내는 N개의 정수가 공백으로 구분되어 시간순
    Y = list(map(int, input().split()))  # 세 번째 줄에는 두 번째 파형 Y의 시간 별 높이가 같은 형식으로 주어진다.

    print(solve(N, X, Y))