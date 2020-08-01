max_value = 0


def solve(N, K, things):
    global max_value

    thing_num = len(things)
    dp = [[0] * (K + 1) for _ in range(thing_num)]
    for i in range(1, thing_num):
        for j in range(1, K + 1):
            if j >= things[i][0]:  # 현재 고려하고있는 가방보다 물건의 무게가 더 작으면
                dp[i][j] = max(dp[i - 1][j], things[i][1] + dp[i - 1][j - things[i][0]])
            else:
                dp[i][j] = dp[i - 1][j]
            max_value = max(max_value, dp[i][j])
            # print('max vlalue',max_value)
            # print('i,j ',i,j)
    # print(dp)

    return max_value


if __name__ == '__main__':
    N, M = map(int, input().split())
    things = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(tmp[2]):
            things.append(tmp[0:2])
    things = [0] + things
    print(solve(N, M, things))

