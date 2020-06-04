# 위, 아래, 왼, 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    N, M, T = map(int, input().split()) # T is rotate_count
    circles = [list(map(int, input().split())) for _ in range(N)]
    circles.insert(0, [])
    rotate_infos = [list(map(int, input().split())) for _ in range(T)]

    for rotate in rotate_infos:
        x, d, k = rotate
        # 1. x의 배숭인 ㅇ원판을 di 방향으로 ki칸 회전시킨다. di 가 0인 경우에는 시계방향, 1인 경ㅇ우는 반시계방향이다.
        cnt = 1
        circle_idx = x * cnt
        while circle_idx <= N:
            if d:
                # 반시계
                circles[circle_idx] = circles[circle_idx][k:] + circles[circle_idx][:k]
            else:
                # 시
                circles[circle_idx] = circles[circle_idx][-k:] + circles[circle_idx][:-k]
            circle_idx += x
        # print_matrix(circles)

        # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
        removable_set = set()
        for i in range(1, N + 1):
            for j in range(0, M):
                if circles[i][j] != 0:
                    for k in range(4):
                        next_x = i + dx[k]
                        next_y = j + dy[k]
                        if 1 <= next_x < N + 1 and 0 <= next_y < M and circles[i][j] == circles[next_x][next_y]:
                                removable_set.add((next_x, next_y))
                        elif 1 <= next_x < N + 1 and (next_y == -1 or next_y == M):
                            if next_y == M:
                                next_y = 0
                  1          if circles[i][j] == circles[next_x][next_y]:
                                removable_set.add((next_x, next_y))
        if removable_set:
            while removable_set:
                temp_x, temp_y = removable_set.pop()
                circles[temp_x][temp_y] = 0
        else:
            # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
            total_sum = 0
            total_count = 0
            for m in range(1, N + 1):
                for n in range(0, M):
                    if circles[m][n] != 0:
                        total_sum += circles[m][n]
                        total_count += 1
            if total_count == 0:
                avg = 0
            else:
                avg = total_sum / total_count

            for m in range(1,N + 1):
                for n in range(0, M):
                    if circles[m][n] != 0:
                        if circles[m][n] > avg:
                            circles[m][n] -= 1
                            # total_sum -= 1
                        elif circles[m][n] < avg:
                            circles[m][n] += 1
                            # total_sum += 1
        # print_matrix(circles)
    answer = 0
    # print(circles)
    for row in circles:
        answer += sum(row)
    print(answer)

