import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == '__main__':
    N, M, P = map(int, input().split())
    S = [0] + list(map(int, input().split()))
    matrix = [['0']*(M+1)] + [['0'] + list(input()) for _ in range(N)]
    visited = [[False] * (M+1) for _ in range(N+1)]
    castle = [0]*(P+1)
    heap = []
    # print(matrix)
    # print(visited)
    # TODO : 반복문 처리 필요하고, 0개늘어나면 종료처리
    while True:
        checksum = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if '1' <= matrix[i][j] <= '9':
                    # print(matrix[i][j])
                    heapq.heappush(heap,(matrix[i][j], 0, i,j))

        # print('caste : {}'.format(castle))
        while heap:
            player_str, depth_num, x, y = heapq.heappop(heap)
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 1<=next_x<=N and 1<=next_y<=M and visited[next_x][next_y] is False and matrix[next_x][next_y] == '.' and depth_num + 1 <= S[int(player_str)]:
                    matrix[next_x][next_y] = player_str
                    heapq.heappush(heap, (matrix[next_x][next_y], depth_num+1, next_x, next_y))

                    checksum += 1
        if checksum == 0:
            break

    # count
    for i in range(1, N+1):
        for j in range(1, M+1):
            if '1' <= matrix[i][j] <= '9':
                castle[int(matrix[i][j])] += 1



    # print_matrix(matrix)
    # print('caste : {}'.format(castle))
    for i in range(1,P+1):
        print(castle[i], end=' ')











