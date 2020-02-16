from copy import deepcopy


def add_vertical_road():
    for i in range(len(matrix)):
        temp = []
        for row in matrix:
            temp.append(row[i])
        roads.append(temp)



def is_available(road):
    visited = [False] * len(road)  # 경사로 놓은칸은 방문 체크

    idx = 0
    while idx < len(road)-1:
        current_height = road[idx]
        next_height = road[idx+1]
        if next_height == current_height:
            pass
        elif next_height == current_height + 1:
            for i in range(L):
                if not (0 <= idx - i <= len(road)-1) or visited[idx - i]:
                    return False
                else:
                    visited[idx - i] = True
        elif next_height == current_height - 1:
            for i in range(1, L+1):
                if 0 <= idx + i <= len(road)-1:
                    if visited[idx + i]:
                        return False
                    else:
                        visited[idx + i] = True
                else:
                    return False
        else:
            return False

        idx += 1
    return True


def solution1():
    available_road_num = 0

    for road in roads:
        if is_available(road):
            available_road_num += 1
    return available_road_num


if __name__ == '__main__':
    N, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    roads = deepcopy(matrix)
    add_vertical_road()

    print(solution1())

