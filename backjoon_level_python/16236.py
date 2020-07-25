from collections import deque

INIT_SHARK_SIZE = 2

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 질문. 가장 가까운 물고기를 구할 때 어떻게 하는 것이 좋은가?
# 1. bfs ? 그렇다면 같은 거리에서의 bfs큐에서 나오는 것들끼리 다시 가장 높은것, 가장 왼쪽에 있는것을 골라야하는가?
def get_nearest_fish(current_shark_location, current_shark_size, can_eat_fish_list):
    x, y = current_shark_location
    visited = [[False]*N for _ in range(N)]
    temp_q_for_return = []

    result_fish_size = -1
    result_fish_x = -1
    result_fish_y = -1
    result_distance = -1

    dq = deque()
    dq.append((0, x, y))
    visited[x][y] = True
    while dq:
        distance, current_x, current_y = dq.popleft()
        if (matrix[current_x][current_y], current_x, current_y) in can_eat_fish_list:
            result_distance = distance
            temp_q_for_return.append((distance, current_x, current_y))

        if result_distance != -1:
            continue

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] is False and matrix[next_x][next_y] <= current_shark_size:
                dq.append((distance + 1, next_x, next_y))
                visited[next_x][next_y] = True
    if temp_q_for_return:
        # print('temp_q_for_return',temp_q_for_return)
        temp_q_for_return.sort(key=lambda x:(x[0],x[1],x[2]))
        nearest_fish = temp_q_for_return[0]
        result_distance, result_fish_x, result_fish_y = nearest_fish
        return matrix[result_fish_x][result_fish_y], result_fish_x, result_fish_y, result_distance
    else:
        return -1,-1,-1,-1




def solve(N, matrix):
    answer = 0

    current_shark_size = INIT_SHARK_SIZE
    current_shark_experience = 0

    shark_dict, current_shark_location = get_shark_info_dict(N, matrix)
    # print('shark dict: ', shark_dict)
    # print('shart location :', current_shark_location)

    can_eat_fish_list = shark_dict[1]
    while can_eat_fish_list:
        fish_size, x, y, distance = get_nearest_fish(current_shark_location, current_shark_size, can_eat_fish_list)
        # print('가장 가까운(잡아먹을) 상어: ')
        # print('fish_size : {} , x : {}, y : {}, distance : {}'.format(fish_size, x, y, distance))
        if fish_size == -1:
            break  # 갈 수 있는 상어가 없음.

        answer += distance

        can_eat_fish_list.remove((fish_size, x, y))
        current_shark_experience += 1
        current_shark_location = (x,y)
        if current_shark_experience == current_shark_size:
            # print('{} => {} level up'.format(current_shark_size, current_shark_size+1))
            current_shark_size += 1
            if current_shark_size -1 <= 6:
                can_eat_fish_list += shark_dict[current_shark_size - 1]
            current_shark_experience = 0

    return answer


def get_shark_info_dict(N, matrix):
    result = {}
    result_shark_location = ()

    for i in range(1, 7):
        result[i] = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                result_shark_location = (i, j)
                matrix[i][j] = 0
            key = matrix[i][j]
            if 1 <= key <= 6:
                result[key].append((matrix[i][j], i, j))
    return result, result_shark_location


if __name__ == '__main__':
    N = int(input())  # 공간의 크기 N(2 ≤ N ≤ 20)
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(solve(N, matrix))

# 예제 4
# 순서:
# 35 10 6 5 7 21
# 11 9 4 8 19 20
# 12 13 0 18 23 22
# 14 1 3 17 24 25
# 15 16 2 28 27 26
# 32 31 30 29 33 34