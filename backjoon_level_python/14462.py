import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def solve2(N, left, right):
    dp = [[-1] * N for _ in range(N)]
    # print(left)
    # print(right)

    def find(s, e):
        if s >= N or e >= N:
            return 0
        if dp[s][e] != -1:
            return dp[s][e]

        current_count = 0
        if abs(left[s]-right[e]) <= 4:
            current_count = 1
        dp[s][e] = max(find(s+1,e), find(s, e+1), find(s+1,e+1)+current_count)
        return dp[s][e]

    answer = find(0, 0)
    return answer




if __name__ == '__main__':
    N = int(input())
    left = [int(input()) for _ in range(N)]
    right = [int(input()) for _ in range(N)]

    print(solve2(N, left, right))