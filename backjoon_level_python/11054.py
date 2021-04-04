def solve(N, arr):
    forward_dp = [1] * N
    backward_dp = [1] * N
    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                forward_dp[i] = max(forward_dp[i], forward_dp[j]+1)
            if arr[N-i-1] > arr[N-j-1]:
                backward_dp[N-i-1] = max(backward_dp[N-i-1], backward_dp[N-j-1] + 1)
    return max([x + y for x, y in zip(forward_dp, backward_dp)]) - 1


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    print(solve(N, numbers))