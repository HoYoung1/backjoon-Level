# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미
import sys

dx = [sys.maxsize, -1,1,0,0]
dy = [sys.maxsize, 0,0,1,-1]



def solve(RR, CC, MM, shark_infos):
    def move(r, c, s, d, z):
        next_r = r
        next_c = c
        if d == 1 or d == 2:
            s = s % (2 * (RR - 1))
        else:
            s = s % (2 * (CC - 1))
        for i in range(s):
            next_r = next_r + dx[d]
            next_c = next_c + dy[d]
            if not (1 <= next_r <= RR) or not (1 <= next_c <= CC):
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3
                next_r = next_r + dx[d]
                next_c = next_c + dy[d]
                next_r = next_r + dx[d]
                next_c = next_c + dy[d]
        return next_r, next_c, s, d, z

    answer = 0
    for time in range(1, CC + 1):
        # 1. 소팅
        shark_infos.sort(key=lambda shark_info: (shark_info[1], shark_info[0], -shark_info[4]))
        # 2. 중복제거
        new_shark_infos = []
        for i in range(len(shark_infos)):
            if i == 0:
                new_shark_infos.append(shark_infos[i])
            else:
                if shark_infos[i - 1][0] == shark_infos[i][0] and shark_infos[i - 1][1] == shark_infos[i][1]:
                    continue
                else:
                    new_shark_infos.append(shark_infos[i])
        # 3. 낚시
        remove_target = None
        for idx, shark_info in enumerate(new_shark_infos):
            if shark_info[1] == time:
                remove_target = idx
                answer += shark_info[4]
                break
        if remove_target is not None:
            del new_shark_infos[remove_target]

        # 4. 무빙
        for idx, shark_info in enumerate(new_shark_infos):
            r, c, s, d, z = shark_info
            new_shark_infos[idx] = move(r,c,s,d,z)

        shark_infos = new_shark_infos
    return answer

if __name__ == '__main__':
    R, C, M = map(int, input().split())
    shark_infos = [list(map(int, input().split())) for _ in range(M)]

    print(solve(R, C, M, shark_infos))

#     exa = ["4 1 3 3 8", "1 3 5 2 9", "2 4 8 4 1", "4 5 0 1 4", "3 3 1 2 7", "1 5 8 4 3", "3 6 2 1 2", "2 2 2 3 5"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(4, 6, 8, exa) == 22
#     assert solve(100, 100, 0, []) == 0
#
#     exa = ["4 1 3 3 8", "1 3 5 2 9", "2 4 8 4 1", "4 5 0 1 4"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(4, 5, 4, []) == 0
#
#     exa = ["1 1 1 1 1", "2 2 2 2 2", "1 2 1 2 3", "2 1 2 1 4"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     assert solve(2, 2, 4, exa) == 4
#
#     assert solve(100, 3, 2, [[2, 3, 0, 1, 2], [4, 3, 1, 1, 3]]) == 3
#
#     exa = ["3 2 2 3 9", "3 3 1 3 3", "3 5 1 4 7", "3 6 2 4 6", "2 4 1 2 8", "1 4 2 2 4", "4 4 1 1 5"]
#     for i in range(len(exa)):
#         exa[i] = list(map(int, exa[i].split()))
#     # assert solve(100, 7, 7, exa) == 0
#
#     assert solve(5, 5, 1, [[1, 4, 10, 3, 1]]) == 0
#
#     assert solve(2, 3, 3, [[1, 3, 2, 4, 1], [1, 2, 1, 4, 2], [1, 1, 2, 3, 4]]) == 4
#     assert solve(2, 5, 2, [[1, 4, 2, 2, 10], [1, 2, 2, 3, 20]]) == 0
#     assert solve(2, 5, 1, [[1, 5, 1, 3, 1]]) == 1
#     assert solve(4, 2, 2, [[2, 2, 3, 1, 1, ], [4, 2, 3, 1, 2]]) == 2
#     assert solve(10, 10, 2, [[1, 9, 8, 2, 1], [5, 10, 7, 4, 2]]) == 0
#
#     assert solve(3, 3, 9,
#                  [[1, 1, 1000, 1, 1], [1, 2, 999, 2, 2], [2, 1, 1000, 3, 3], [2, 2, 999, 4, 4], [1, 3, 1000, 1, 5],
#                   [3, 1, 999, 2, 6], [2, 3, 1000, 3, 7], [3, 2, 999, 4, 8], [3, 3, 1000, 1, 9]]) == 8
#
#     assert solve(10, 10, 2, [[1, 9, 8, 2, 1], [5, 10, 7, 4, 2]]) == 0
#     assert solve(4, 2, 2, [[2, 2, 3, 1, 1], [4, 2, 3, 1, 2]]) == 2
#
#     assert solve(2, 5, 1, [[1, 5, 1, 3, 1]]) == 1
#     assert solve(5, 5, 1, [[1, 4, 10, 3, 1]]) == 0
#     assert solve(3, 3, 1, [[2, 2, 1, 3, 1]]) == 0
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
# solve(50, 50, 19, exa) == 7718
