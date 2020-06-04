answer = 0


# O(2^n)
# 런타임 에러
def solve1(N, K, stocks):
    def dfs(depth, length):
        global answer
        if length == K:
            answer = 1
        if answer == 1:
            return
        if K + len(stocks) < depth or depth == len(stocks) - 1:
            return
        if stocks[depth] < stocks[depth + 1]:
            dfs(depth + 1, length + 1)
        dfs(depth + 1, length)

    dfs(0, 1)
    return answer

# pypy3
# 125560KB 5092ms
# O(n^2)
def solve2(N, K, stocks):
    dp = [1]*N

    result = 0
    if K == 1:
        result = 1

    for i in range(0, N):
        for j in range(0, i):
            if stocks[j] < stocks[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
                if dp[i] >= K:
                    result = 1
    return result


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        answer = 0
        N, K = map(int, input().split())
        stocks = list(map(int, input().split()))
        print('Case #{}'.format(i+1))
        print(solve2(N, K, stocks))

    assert solve2(10, 6, [100, 50, 70, 90, 75, 87, 105, 78, 110, 60]) == 1
    assert solve2(10, 10, [100, 50, 70, 90, 75, 87, 105, 78, 110, 60]) == 0
    assert solve2(1, 1, [100]) == 1
    assert solve2(2, 1, [100, 50]) == 1
    assert solve2(2, 2, [100, 50]) == 0
    assert solve2(2, 2, [50, 100]) == 1
    assert solve2(6, 3, [100, 90, 80, 70, 60, 50]) == 0
    assert solve2(10, 4, [8, 11, 9, 7, 4, 6, 12, 13, 5, 10]) == 1

