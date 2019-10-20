from collections import deque

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)


def get_available_direction(type_s):
    if type_s == 1:
        available_direction = [left, right, up, down]
    elif type_s == 2:
        available_direction = [up, down]
    elif type_s == 3:
        available_direction = [left, right]
    elif type_s == 4:
        available_direction = [up, right]
    elif type_s == 5:
        available_direction = [down, right]
    elif type_s == 6:
        available_direction = [left, down]
    elif type_s == 7:
        available_direction = [left, up]

    try:
        available_direction
    except Exception as e:
        print(e)

    return available_direction


def is_connected(b_xy, tunnel_xy, t_map):
    temp_list = get_available_direction(t_map[b_xy[0]][b_xy[1]])
    for direction in temp_list:
        if direction == left:
            direction = right
        elif direction == right:
            direction = left
        elif direction == up:
            direction = down
        elif direction == down:
            direction = up
    inter = set(temp_list) & set(get_available_direction(t_map[tunnel_xy[0]][tunnel_xy[1]]))
    if inter:
        return True
    return False


def arrest(N, M, R, C, L, t_map, searched, rtn_val):
    """

    :param searched:
    :param rtn_val:
    :param N: 행
    :param M: 열
    :param R: 맨홀 뚜겅이 위치한 세로위치
    :param C: 맨홀 뚜겅이 위치한 가로위치
    :param L: 탈출 후 소요된 시간 L
    :param t_map: 2차원 리스트
    :return exist_loc: 있을수있는 장소
    """
    timer = 1
    dq = deque([(R, C, timer)])
    searched.append((R, C))
    rtn_val += 1
    while dq:
        tunnel_xy = dq.popleft()
        for direction in get_available_direction(t_map[tunnel_xy[0]][tunnel_xy[1]]):
            x = tunnel_xy[0] + direction[0]
            y = tunnel_xy[1] + direction[1]
            timer = tunnel_xy[2]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if (x, y) in searched or t_map[x][y] == 0 or not is_connected((x, y), tunnel_xy, t_map) or timer+1 > L:
                continue
            searched.append((x, y))
            dq.append((x, y, timer+1))
            rtn_val += 1


    return rtn_val


if __name__ == '__main__':
    for i in range(int(input())):
        N, M, R, C, L = map(int, input().split())

        grid = [list(map(int, input().split())) for _ in range(N)]
        searched = []
        rtn_val = 0
        print('#{} {}'.format(i + 1, arrest(N, M, R, C, L, grid, searched, rtn_val)))
