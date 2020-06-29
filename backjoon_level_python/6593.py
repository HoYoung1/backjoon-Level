from collections import deque# 동서 남북 상하dz = [0, 0, 0, 0, -1, 1]dx = [0, 0, 1, -1, 0, 0]dy = [1, -1, 0, 0, 0, 0]def solve(building, start_location, escape_location):    visited = [[[False] * C for _ in range(R)] for _ in range(L)]    dq = deque()    s_z, s_x, s_y = start_location    dq.append((s_z, s_x, s_y, 0))    visited[s_z][s_x][s_y] = True    while dq:        z, x, y, current_time = dq.popleft()        if (z, x, y) == escape_location:            return 'Escaped in {} minute(s).'.format(current_time)        for i in range(6):            next_z = z + dz[i]            next_x = x + dx[i]            next_y = y + dy[i]            if 0 <= next_z < L and 0 <= next_x < R and 0 <= next_y < C and visited[next_z][next_x][next_y] is False and building[next_z][next_x][next_y] != '#':                dq.append((next_z, next_x, next_y, current_time + 1))                visited[next_z][next_x][next_y] = True    return 'Trapped!'if __name__ == '__main__':    while True:        L, R, C = map(int, input().split())        if L == 0 and R == 0 and C == 0:            break        building = [[[0] * C for _ in range(R)] for _ in range(L)]  # init        for i in range(L):            for j in range(R):                building[i][j] = list(input())                for k in range(C):                    if building[i][j][k] == 'S':                        start_location = (i, j, k)                    elif building[i][j][k] == 'E':                        escape_location = (i, j, k)            _ = input()        print(solve(building, start_location, escape_location))