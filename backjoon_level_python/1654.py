def solve(K, N, lans):
    start = 1
    end = sum(lans) // N
    # answer = 0
    while start <= end:
        mid = (start + end) // 2
        count = sum([lan // mid for lan in lans])
        if count >= N:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


if __name__ == '__main__':
    K, N = map(int, input().split())
    lans = [int(input()) for _ in range(K)]

    print(solve(K, N, lans))