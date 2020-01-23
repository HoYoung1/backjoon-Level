class Cogwheel:
    def __init__(self, state):
        self.state = state

    def _rotate_right(self):  # 시계
        self.state = self.state[-1] + self.state[0:7]

    def _rotate_left(self):  # 반시계
        self.state = self.state[1:8] + self.state[0]

    def rotate(self, direction):
        if direction == 1:
            self._rotate_right()
        elif direction == -1:
            self._rotate_left()

    def left_mesh_point(self):
        return self.state[6]

    def right_mesh_point(self):
        return self.state[2]


def recursive_rotate(cogwheel_num, direction):
    global check_rotated

    if check_rotated[cogwheel_num] is True:
        # 이미 회전한 톱니바퀴
        return
    else:
        check_rotated[cogwheel_num] = True

    # 왼쪽 혹은 오른쪽 톱니바퀴와 맞물리는지 검사
    current_left_mesh, current_right_mesh = \
        cogwheels[cogwheel_num].left_mesh_point(), cogwheels[cogwheel_num].right_mesh_point()

    if cogwheel_num != 0:
        # 제일 왼쪽 끝이 아니라면
        left_wheel_right_mesh = cogwheels[cogwheel_num - 1].right_mesh_point()
        if current_left_mesh != left_wheel_right_mesh:
            # 물려있으면
            recursive_rotate(cogwheel_num - 1, direction * -1)
    if cogwheel_num != T-1:
        # 제일 오른쪽 끝이 아니라면
        right_wheel_left_mesh = cogwheels[cogwheel_num + 1].left_mesh_point()
        if current_right_mesh != right_wheel_left_mesh:
            # 물려있으면
            recursive_rotate(cogwheel_num + 1, direction * -1)

    cogwheels[cogwheel_num].rotate(direction)


if __name__ == '__main__':
    # COGWHEEL_NUM = 4
    # cogwheels = [Cogwheel(input()) for _ in range(COGWHEEL_NUM)]

    T = int(input())
    cogwheels = [Cogwheel(input()) for _ in range(T)]

    for _ in range(int(input())):
        gear_num, direction = map(int, input().split())
        check_rotated = [False] * T
        gear_num -= 1  # 입력값은 1부터~, 하지만 인덱스는 0부터
        recursive_rotate(gear_num, direction)

    # # for debugging
    # for i in range(COGWHEEL_NUM):
    #     print(cogwheels[i].state)

    total_point = 0
    for i in range(T):
        if cogwheels[i].state[0] == '1':
            # S극이면
            total_point += 1

    print(total_point)




