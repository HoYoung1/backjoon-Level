import sys
from enum import Enum


class Messages(Enum):
    CRASH_INTO_WALL = 'Robot {} crashes into the wall'
    CRASH_INTO_ROBOT = 'Robot {} crashes into robot {}'


class Command(Enum):
    LEFT_90 = 'L'
    RIGHT_90 = 'R'
    FORWARD = 'F'


class RobotDirection(Enum):
    NORTH = 'N'
    WEST = 'W'
    SOUTH = 'S'
    EAST = 'E'


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def convert(x: str, y: str) -> (int, int):
    return B - int(x), int(y) - 1,


def find_index_with_direction(direction: str):
    for idx, robot_direction in enumerate(RobotDirection):
        if direction == robot_direction.value:
            return idx


def solve():
    global B, matrix
    A, B = map(int, input().split())
    matrix = [[0] * A for _ in range(B)]
    N, M = map(int, input().split())
    robots = [[]] * N

    # locations
    locations = [input().split() for _ in range(N)]
    for i in range(N):
        y, x, d = locations[i]
        x, y = convert(x, y)
        matrix[x][y] = i + 1  # 지도에 로봇 인덱스를 표시
        robots[i] = (x, y, d)

    # orders
    orders = [input().split() for _ in range(M)]
    for i in range(M):
        robot_idx, cmd, count = orders[i]
        robot_idx, count = int(robot_idx) - 1, int(count)  # convert

        if cmd == Command.FORWARD.value:
            for _ in range(count):
                x, y, d = robots[robot_idx]  # get_robot_info

                next_x = None
                next_y = None
                for idx, robot_direction in enumerate(RobotDirection):
                    if d == robot_direction.value:
                        next_x = x + dx[idx]
                        next_y = y + dy[idx]
                        break

                if not (0 <= next_x < B and 0 <= next_y < A):
                    print(Messages.CRASH_INTO_WALL.value.format(robot_idx + 1))
                    return
                elif matrix[next_x][next_y] != 0:  # 다른 로봇이 있으면
                    print(Messages.CRASH_INTO_ROBOT.value.format(robot_idx + 1, matrix[next_x][next_y]))
                    return
                else:
                    matrix[x][y] = 0  # 지도에 빈 표시
                    matrix[next_x][next_y] = robot_idx + 1  # 갱신
                    robots[robot_idx] = (next_x, next_y, d)
        elif cmd == Command.LEFT_90.value:
            x, y, d = robots[robot_idx]  # get_robot_info
            robots[robot_idx] = (x, y, list(RobotDirection)[(find_index_with_direction(d) + count) % 4].value)  # NWSE

        elif cmd == Command.RIGHT_90.value:
            x, y, d = robots[robot_idx]  # get_robot_info
            robots[robot_idx] = (x, y, list(RobotDirection)[(find_index_with_direction(d) - count) % 4].value)
    print("OK")


if __name__ == '__main__':
    # for z in range(int(input())):
    solve()

