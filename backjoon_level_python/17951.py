def solve(N, K, scores):
    max_score = N * 20

    left = 0
    right = max_score
    answer = 0

    while left<=right:
        mid = (left + right) // 2

        current_count = 0
        current_sum = 0
        for i in range(N):
            current_sum += scores[i]
            if current_sum >= mid:
                current_count += 1
                current_sum = 0
            if current_count == K:
                left = mid+1
                answer = max(answer, mid)
                break
        else:
            right = mid-1
    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    print(solve(N, K, scores))


    # assert solve(8, 2, [12, 7, 19, 20, 17, 14, 9, 10]) == 50
    # assert solve(8, 2, [0, 0, 0, 0, 0, 0, 0, 0]) == 0
    # assert solve(4, 2, [2, 3, 5, 7]) == 7