# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미

dx = [-10, -1, 1, 0, 0]
dy = [-10, 0, 0, 1, -1]


def move_shark(R, C, r, c, s, d, z):
    # 1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000)
    next_r = r
    next_c = c
    if d ==1 or d== 2:
        s = s % (2*(R-1))
    else:
        s = s % (2 * (C-1))
    for i in range(s):
        next_r = next_r + dx[d]
        next_c = next_c + dy[d]
        if not (1<=next_r<=R) or not (1<=next_c<=C):
            # 방향 회전
            if d == 1 or d == 3:
                d += 1
            else:
                d -= 1
            next_r = next_r + dx[d]
            next_c = next_c + dy[d]
            next_r = next_r + dx[d]
            next_c = next_c + dy[d]
    return next_r, next_c, s, d, z


def solve(R,C,M, next_shark_infos):
    total_fish_size = 0

    next_shark_infos.sort(key=lambda next_shark_info:next_shark_info[1])
    for t in range(1,C+1):
        
        # 상어 잡기 먼저함
        target_shark = None
        for i in range(len(next_shark_infos)):
            # 낚시할 수 있는 상어있는지 봄
            if next_shark_infos[i][1] == t:
                target_shark = i
                total_fish_size += next_shark_infos[i][4]
                break
        if target_shark is not None:
            del next_shark_infos[target_shark]

        # 상어를 움직임
        updated_next_shark_infos = []
        for shark_info in next_shark_infos:
            r, c, s, d, z = shark_info
            next_shark_info = move_shark(R,C, r, c, s, d, z)
            updated_next_shark_infos.append(next_shark_info)

        updated_next_shark_infos.sort(key=lambda updated_next_shark_info:(updated_next_shark_info[1], updated_next_shark_info[0], -updated_next_shark_info[4]))

        # 움직여진 상어들중 겹치는것이 있는지 본다
        next_shark_infos = []
        for i in range(len(updated_next_shark_infos)):

            if 1 <= i and updated_next_shark_infos[i][0] == updated_next_shark_infos[i-1][0] and updated_next_shark_infos[i][1] == updated_next_shark_infos[i-1][1]:
                continue
                # 겹친 상어는 빠짐
            next_shark_infos.append(updated_next_shark_infos[i])

    return total_fish_size


if __name__ == '__main__':
    R, C, M = map(int ,input().split())
    shark_infos = [list(map(int, input().split())) for _ in range(M)]

    print(solve(R,C,M, shark_infos))

#     exa = ["4 1 3 3 8", "1 3 5 2 9", "2 4 8 4 1", "4 5 0 1 4", "3 3 1 2 7", "1 5 8 4 3", "3 6 2 1 2", "2 2 2 3 5"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(4,6,8,exa) == 22
#     assert solve(100,100,0,[]) == 0
#
#     exa = ["4 1 3 3 8", "1 3 5 2 9", "2 4 8 4 1", "4 5 0 1 4"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(4, 5, 4, []) == 0
#
#     exa = ["1 1 1 1 1", "2 2 2 2 2", "1 2 1 2 3", "2 1 2 1 4"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(2,2,4,exa) == 4
#
#     assert solve(100,3,2,[[2,3,0,1,2],[4,3,1,1,3]]) == 3
#
#     exa = ["3 2 2 3 9", "3 3 1 3 3", "3 5 1 4 7", "3 6 2 4 6", "2 4 1 2 8", "1 4 2 2 4", "4 4 1 1 5"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(100,7,7,exa) == 0
#
#     assert solve(5,5,1,[[1,4,10,3,1]]) == 0
#
#     assert solve(2,3,3,[[1,3,2,4,1],[1,2,1,4,2],[1,1,2,3,4]]) == 4
#     assert solve(2,5,2,[[1,4,2,2,10], [1,2,2,3,20]]) == 0
#     assert solve(2,5,1,[[1,5,1,3,1]]) == 1
#     assert solve(4,2,2,[[2,2,3,1,1,], [4,2,3,1,2]]) == 2
#     assert solve(10,10,2,[[1,9,8,2,1],[5,10,7,4,2]]) == 0
#
#     assert solve(3,3,9,[[1,1,1000,1,1],[1,2,999,2,2],[2,1,1000,3,3],[2,2,999,4,4],[1,3,1000,1,5],[3,1,999,2,6],[2,3,1000,3,7],[3,2,999,4,8],[3,3,1000,1,9]]) == 8
#
#     assert solve(10,10,2,[[1,9,8,2,1],[5,10,7,4,2]]) == 0
#     assert solve(4,2,2,[[2,2,3,1,1],[4,2,3,1,2]]) == 2
#
#     assert solve(2, 5, 1, [[1,5,1,3,1]]) == 1
#     assert solve(5, 5, 1, [[1, 4, 10, 3, 1]]) == 0
#     assert solve(3,3,1,[[2,2,1,3,1]]) == 0
#
#     exa = """4 9 21 1 999
# 50 50 4 4 500
# 50 49 222 3 200
# 50 48 12 2 45
# 50 47 36 1 900
# 2 3 20 3 444
# 4 8 4 2 49
# 3 3 40 4 50
# 2 2 460 2 4444
# 48 23 500 3 12
# 1 1 200 1 123
# 44 44 123 3 125
# 44 40 222 3 17
# 40 44 333 3 57
# 18 40 1 1 4
# 3 10 50 2 406
# 1 36 177 4 50
# 1 46 120 4 7
# 1 50 28 4 54""".split('\n')
# for i in range(len(exa)):
#     exa[i] = list(map(int, exa[i].split()))
# solve(50,50,19,exa) == 7718
