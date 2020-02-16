import enum

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


class LandState(enum.Enum):
    EMTPY = 0
    WALL = 1
    CLEANED = 2


class Robot:
    def __init__(self, direction, location):
        self.direction = direction  # d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
        self.r, self.c = location
        self.clean_room_num = 0

    def clean_current_location(self):
        if get_location_status(self.r, self.c) != LandState.CLEANED:
            matrix[self.r][self.c] = LandState.CLEANED
            self.clean_room_num += 1

    def check_left_wall(self):
        temp_direction = (self.direction - 1) % 4
        temp_r = self.r + dx[temp_direction]
        temp_c = self.c + dy[temp_direction]
        return matrix[temp_r][temp_c]

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def move_forward(self):
        self.r += dx[self.direction]
        self.c += dy[self.direction]

    def move_backward(self):
        self.r += dx[self.direction] * -1
        self.c += dy[self.direction] * -1

    def available_back(self):
        temp_r = self.r + dx[self.direction] * -1
        temp_c = self.c + dy[self.direction] * -1
        if get_location_status(temp_r, temp_c) == LandState.WALL:
            return False
        return True

    def all_direction_cleaned_or_wall(self):
        for i in range(4):
            if get_location_status(self.r + dx[i], self.c + dy[i]) == LandState.EMTPY:
                return False
        return True

    def run(self):
        status = 1
        while True:
            # for debugging
            for line in matrix:
                for i in line:
                    print(i.value, end="")
                print()
            print()
            print("현재 나의 direction : ", self.direction)
            print()
            if get_location_status(9, 1) == LandState.CLEANED:
                print(1)
                pass

            if status <= 1:
                self.clean_current_location()
            if status <= 2:
                if self.check_left_wall() == LandState.EMTPY:
                    self.turn_left()
                    self.move_forward()
                    status = 1
                else:
                    if self.all_direction_cleaned_or_wall():
                        if self.available_back():
                            self.move_backward()
                            status = 2
                        else:
                            break
                    else:
                        self.turn_left()
                        status = 2


def solution():
    robot = Robot(d, (r, c))
    robot.run()
    return robot.clean_room_num


def get_location_status(x, y):
    return matrix[x][y]


if __name__ == '__main__':
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    matrix = [[LandState.EMTPY if x == '0' else LandState.WALL for x in input().split()] for _ in range(N)]
    print(solution())
