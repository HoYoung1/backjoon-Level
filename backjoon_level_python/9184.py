def solve(a, b, c):
    return func(a, b, c)


def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
    return dp[a][b][c]


if __name__ == '__main__':
    dp = [[[-1] * 21 for _ in range(21)] for _ in range(21)]
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = {solve(a,b,c)}')