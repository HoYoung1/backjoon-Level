import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    n = int(input())
    matrix = [[1]*n for _ in range(n)]

    # 맵 셋팅
    start_x, start_y, end_x, end_y = map(lambda x:int(x)-1, input().split())
    k = int(input())
    circuit_num = int(input())
    for i in range(circuit_num):
        path_input = list(map(lambda x: int(x)-1, input().split()))[1:]
        for j in range(len(path_input)//2-1):
            x, y = path_input[2*j], path_input[2*j+1]
            n_x, n_y = path_input[2*(j+1)], path_input[2*(j+1)+1]
            if x == n_x:
                if y > n_y:
                    while y >= n_y:
                        matrix[x][y] = k
                        y -= 1
                else:
                    while y <= n_y:
                        matrix[x][y] = k
                        y += 1
            elif y == n_y:
                if x > n_x:
                    while x >= n_x:
                        matrix[x][y] = k
                        x -= 1
                else:
                    while x <= n_x:
                        matrix[x][y] = k
                        x += 1

    # 다익스트라 From start to end
    distance_matrix = [[-1] * n for _ in range(n)]
    hq = []
    distance_matrix[start_x][start_y] = matrix[start_x][start_y]
    heapq.heappush(hq, (matrix[start_x][start_y], start_x, start_y))
    while hq:
        d, x, y = heapq.heappop(hq)
        # if x == end_x and y == end_y:
        #     print('x, y', x, y)
        #     print('d')
        #     print(d)
        #     break
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<n and 0<=n_y<n and distance_matrix[n_x][n_y] == -1: # 방문한적 없으면 -1임
                next_d = d + matrix[n_x][n_y]
                distance_matrix[n_x][n_y] = (next_d, x, y)
                heapq.heappush(hq, (next_d, n_x, n_y))

        # print_matrix(distance_matrix)
    # print_matrix(matrix)
    print(distance_matrix[end_x][end_y][0])

    path_history = []
    target_x, target_y = end_x, end_y
    while True:
        path_history.append((target_x, target_y))
        if target_x == start_x and target_y == start_y:
            break
        _, target_x, target_y = distance_matrix[target_x][target_y]
    # print('path history', path_history)

    left_on = False
    right_on = False

    x, y = path_history[0]
    n_x, n_y = path_history[1]

    if x == n_x:
        right_on = True
    else:
        left_on = True

    answer = []
    for i, path in enumerate(path_history[:-1]):
        x, y = path_history[i]
        n_x, n_y = path_history[i+1]
        if x != n_x and right_on is True:
            left_on = True
            right_on = False
            answer.append((x, y))
        elif y != n_y and left_on is True:
            left_on = False
            right_on = True
            answer.append((x, y))
    print(len(answer)+2, start_x+1, start_y+1, end=" ")
    for a in answer[::-1]:
        print(a[0]+1, a[1]+1, end=" ")
    print(end_x+1, end_y+1)




