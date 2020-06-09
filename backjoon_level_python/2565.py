def lis(N, electric_wires):
    lis_answer = 1
    electric_wires.sort(key=lambda wire: wire[0])
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if electric_wires[j][1] < electric_wires[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
                lis_answer = max(lis_answer, dp[i])
        # print(dp)
    return N - lis_answer


if __name__ == '__main__':
    N = int(input())
    electric_wires = [list(map(int,input().split())) for _ in range(N)]

    print(lis(N, electric_wires))
