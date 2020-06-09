import sys
from collections import deque

def solve(N, matrix):
    result = sys.maxsize
    for x in range(1, N+1):
        for y in range(1, N+1):
            # 시간 초과나면 아래 포문 범위 줄이기
            for d1 in range(1, y):
                for d2 in range(1, N-y+1):
                    if not 1<=y-d1<=N or not 1<=y+d2<=N:
                        print('범위 잘못 설정함 확인')
                    if 1<=x+d2+d1<=N:
                        # 맨 아래쪽이 맵에 벗어나는지 확인. 즉 =선거구를 나눌 수 있음

                        mark = [[0]*len(matrix) for _ in range(len(matrix))]
                        precincts = [0]*5

                        # # 5번 선거구 경계선 표시
                        # for i in range(d1 + 1):
                        #     mark[x + i][y - i] = 5
                        #     precincts[4] += matrix[x + i][y - i]
                        # for i in range(d2 + 1):
                        #     mark[x + i][y + i] = 5
                        #     precincts[4] += matrix[x + i][y + i]
                        # for i in range(d2 + 1):
                        #     mark[x + d1 + i][y - d1 + i] = 5
                        #     precincts[4] += matrix[x + d1 + i][y - d1 + i]
                        # for i in range(d1+1):
                        #     mark[x+d2+i][y+d2-i] = 5
                        #     precincts[4] += matrix[x+d2+i][y+d2-i]
                        # dq = deque()
                        # dq.append((x+1,y))
                        # mark[x+1][y] = 5
                        # visit[x+1][y] = True
                        # precincts[4] += matrix[x+1][y]
                        # dx = [-1, 1, 0, 0]
                        # dy = [0,0,-1,1]
                        # while dq:
                        #     temp_x, temp_y = dq.popleft()
                        #     for kk in range(4):
                        #         next_x = temp_x + dx[kk]
                        #         next_y = temp_y + dy[kk]
                        #         if mark[next_x][next_y] == 0:
                        #             mark[next_x][next_y] = 5
                        #             precincts[4] += matrix[next_x][next_y]
                        #             dq.append((next_x, next_y))



                        for r in range(1, N + 1):
                            for c in range(1, N + 1):
                                if mark[r][c] == 5:
                                    # 경계선임
                                    continue

                                if 1<=r<x+d1 and 1<=c<=y and not (r >=x and c>= y - (r - x)):
                                    precincts[0] += matrix[r][c]
                                    mark[r][c] = 1
                                elif 1<=r<=x+d2 and y<c<=N and not (r>=x and c<=y + (r-x)):
                                    precincts[1] += matrix[r][c]
                                    mark[r][c] = 2
                                elif x+d1<=r<=N and 1<=c<y-d1+d2 and not (r<=x + d1 + d2 and c >= (y - d1 + d2 - (x + d1 + d2 - r))):
                                    precincts[2] += matrix[r][c]
                                    mark[r][c] = 3
                                elif x+d2 < r <=N and y-d1+d2<=c<=N and not (r <= x + d1 + d2 and c <= (y - d1 + d2 + (x + d1 + d2 - r ))):
                                    precincts[3] += matrix[r][c]
                                    mark[r][c] = 4
                                else:
                                    precincts[4] += matrix[r][c]
                                    mark[r][c] = 5
                        result = min(result, max(precincts)-min(precincts))
                        # print('x y d1 d2')
                        # print(x,y,d1,d2)
                        # print_matrix(mark)
                        # print('end')
    return result





def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()



if __name__ == '__main__':
    N = int(input())
    matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
    matrix.insert(0, [0]*(N+1))
    # print_matrix(matrix)
    print(solve(N, matrix))