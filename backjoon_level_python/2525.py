def solve(hh, mm, minute_taken):
    return (hh + (mm + minute_taken) // 60) % 24, (mm + minute_taken) % 60


if __name__ == '__main__':
    A, B = map(int, input().split())
    C = int(input())
    print(' '.join(map(str, solve(A, B, C))))
