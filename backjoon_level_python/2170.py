import sys
input = sys.stdin.readline


def solve(N, matrix):
    answer = 0
    matrix.sort(key=lambda x: x[0])
    current_left, current_right = matrix[0][0], matrix[0][1]

    for l, r in matrix[1:]:
        if current_right < l:
            # 못합침, 계산
            answer += current_right - current_left
            current_left, current_right = l, r
        else:
            current_right = max(current_right, r)
    answer += current_right - current_left
    return answer


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    print(solve(N, matrix))
