max_value = 0

# 좋은 예신
# 1 2
# 1 1


# dfs 시간 초과
def solve1(N, K, things):
    def dfs(depth, this_weight, this_value):
        global max_value

        max_value = max(max_value, this_value)
        if depth + 1 <= N:
            if this_weight + things[depth][0] <= K:
                dfs(depth + 1, this_weight + things[depth][0], this_value + things[depth][1])
            dfs(depth + 1, this_weight, this_value)
    dfs(0, 0, 0)
    return max_value


def solve2(N, K, things):
    global max_value

    things.insert(0, [])
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, K+1):
            if j >= things[i][0]: # 현재 고려하고있는 가방보다 물건의 무게가 더 작으면
                dp[i][j] = max(dp[i-1][j], things[i][1]+dp[i-1][j-things[i][0]])
            else:
                dp[i][j] = dp[i-1][j]
            max_value = max(max_value, dp[i][j])
    # print(dp)
    
    return max_value


if __name__ == '__main__':
    N, K = map(int, input().split())
    things = [tuple(map(int, input().split())) for _ in range(N)]
    print(solve1(N, K, things))
    # print(solve2(N, K, things))

