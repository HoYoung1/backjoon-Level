# https://www.acmicpc.net/problem/2003
# 29532KB 64ms

if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = 0
    accumulation = 0
    start_idx = 0
    for current_idx, number in enumerate(numbers):
        accumulation += number

        while accumulation > M:
            accumulation -= numbers[start_idx]
            start_idx += 1

        if accumulation == M:
            answer += 1
    print(answer)


