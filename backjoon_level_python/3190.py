import queue
import enum


class LandState(enum.Enum):
    EMPTY = 0
    APPLE = 1
    SNAKE = 2
    WALL = 3


class Direction(enum.Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class RotateDirection(enum.Enum):
    LEFT = 'L'
    RIGHT = 'D'


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


class Dummy:
    def __init__(self, matrix):
        self.passed_time = 0
        self.matrix = matrix
        self.snake_body = queue.Queue()
        self.snake_direction = Direction.EAST
        self.snake_head_location = (0, 0)
        self.snake_body.put(self.snake_head_location)  # start position
        self.matrix[0][0] = LandState.SNAKE

    def run(self):
        while True:
            self.passed_time += 1
            self.snake_head_location = self._get_next_location()  # update snake_head
            i, j = self.snake_head_location

            if self._is_wall(i, j) or self.matrix[i][j] == LandState.SNAKE:
                # 게임을 종료한다
                break
            elif self.matrix[i][j] == LandState.APPLE:
                # 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
                self.matrix[i][j] = LandState.SNAKE
            elif self.matrix[i][j] == LandState.EMPTY:
                # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
                tail_i, tail_j = self.snake_body.get()
                self.matrix[tail_i][tail_j] = LandState.EMPTY

            self.matrix[i][j] = LandState.SNAKE
            self.snake_body.put((i, j))

            # 방향 바꿀 시간
            if self._is_time_to_change_direction():
                locate_direction = snake_traffic_line[self.passed_time]
                if locate_direction == RotateDirection.LEFT:
                    self.snake_direction = Direction((self.snake_direction.value - 1) % len(Direction))
                elif locate_direction == RotateDirection.RIGHT:
                    self.snake_direction = Direction((self.snake_direction.value + 1) % len(Direction))

    def get_passed_time(self):
        return self.passed_time

    def _get_next_location(self):
        x, y = self.snake_head_location
        direction = self.snake_direction.value
        return x + dx[direction], y + dy[direction]

    def _is_time_to_change_direction(self):
        return self.passed_time in snake_traffic_line.keys()

    def _is_wall(self, i, j):
        return i < 0 or i >= N or j < 0 or j >= N


def solution():
    dummy = Dummy(matrix)
    dummy.run()
    return dummy.get_passed_time()


if __name__ == '__main__':
    N = int(input())
    matrix = [[LandState.EMPTY] * N for _ in range(N)]

    K = int(input())
    for _ in range(K):
        i, j = map(int, input().split())
        matrix[i - 1][j - 1] = LandState.APPLE

    L = int(input())
    snake_traffic_line = {}
    for _ in range(L):
        t, d = input().split()
        snake_traffic_line[int(t)] = RotateDirection(d)

    print(solution())
