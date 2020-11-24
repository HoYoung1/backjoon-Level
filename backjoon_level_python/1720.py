dp = [0] * 31
if __name__ == '__main__':
    answer = None

    N = int(input())
    dp[0] = 1 # ㅇㅣ 초기값은...이해가안가네 ㅠ
    dp[1] = 1
    dp[2] = 3
    # 홀 수 일 때는 중간의 2 * 1 세로 긴막대기를 중심으로 좌우대칭인거 밖에 없다. 따라서 dp[n / 2]를 더해버리면 된다??
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2] * 2
    # print(dp)
    if N % 2 != 0:
        answer = (dp[N] + dp[N//2]) // 2
    else:
        answer = (dp[N] + dp[N//2] + 2 * dp[N//2-1]) // 2
    print(answer)

