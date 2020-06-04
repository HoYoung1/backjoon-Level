# https://www.acmicpc.net/problem/15686
# 29632 KB, 348ms

# 치킨거리 최솟값
from enum import Enum
from itertools import combinations
import sys

minimum_chicken_distance = sys.maxsize


class LandType(Enum):
    EMPTY = 0
    HOUSE = 1
    CHICKEN = 2


def solve(N, M):
    global minimum_chicken_distance

    # init
    houses = []
    chicken_places = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == LandType.CHICKEN.value:
                chicken_places.append((i, j))
            elif matrix[i][j] == LandType.HOUSE.value:
                houses.append((i, j))

    # get distacne map
    house_distance_map = [[0] * len(chicken_places) for _ in range(len(houses))]
    for house_idx, house in enumerate(houses):
        house_i, house_j = house
        for chicken_idx, chicken_place in enumerate(chicken_places):
            c_place_i, c_place_j = chicken_place
            distance = abs(house_i - c_place_i) + abs(house_j - c_place_j)
            house_distance_map[house_idx][chicken_idx] = distance

    # get chicken distance each house in all of combination
    chicken_combs = list(combinations(range(len(chicken_places)), M))
    for chicken_cob in chicken_combs:
        sum_chicken_distance = 0
        for house_idx, house in enumerate(houses):
            current_chicken_distance = sys.maxsize
            for chicken_place_idx in chicken_cob:
                current_chicken_distance = min(current_chicken_distance, house_distance_map[house_idx][chicken_place_idx])
            sum_chicken_distance += current_chicken_distance
        minimum_chicken_distance = min(minimum_chicken_distance, sum_chicken_distance)

    return minimum_chicken_distance







if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    matrix = [list(map(int,input().split())) for _ in range(N)]

    print(solve(N, M))




