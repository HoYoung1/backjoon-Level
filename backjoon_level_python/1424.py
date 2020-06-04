from math import ceil


def solve(N, L, C):
    temp_c = C
    song_in_cd = 0
    while L <= temp_c:
        song_in_cd += 1
        temp_c -= L
        temp_c -= 1
    if song_in_cd % 13 == 0:
        song_in_cd -= 1

    song_in_last_cd = N % song_in_cd
    if song_in_last_cd == 0:
        song_in_last_cd = song_in_cd

    if song_in_last_cd % 13 == 0:
        if 1 <= song_in_cd - 1 and (song_in_cd - 1) % 13 != 0 and song_in_last_cd + 1 <= song_in_cd:
            return ceil(N/song_in_cd)
        else:
            return ceil(N / song_in_cd) + 1
    else:
        return ceil(N / song_in_cd)


if __name__ == '__main__':
    N = int(input()) # 노래의 갯수 1<=N<100,000
    L = int(input()) # 노래의 길이 1<=L<=C
    C = int(input()) # 시디의 용량 1<=C<10,000

    print(solve(N, L, C))

    # assert solve(1, 1, 1) == 1
    # assert solve(1, 2, 2) == 1
    # assert solve(2, 2, 2) == 2
    # assert solve(2, 4, 8) == 2
    # assert solve(100000,1,10000) == 20
    # assert solve(58, 2, 46) == 4
