def solve(N, K):
    result = 0

    while K:
        coin = coins.pop()
        result += K // coin
        K %= coin
    return result


if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    print(solve(N, K))