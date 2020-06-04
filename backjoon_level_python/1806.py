import sys
#40000KB 128ms


def solve():
    if sum(numbers) < S:
        return 0

    answer = sys.maxsize
    start_idx = 0
    current_sum = 0
    for i in range(len(numbers)):
        current_sum += numbers[i]
        while current_sum >= S:
            answer = min(answer, i - start_idx + 1)
            current_sum -= numbers[start_idx]
            start_idx += 1
    return answer


if __name__ == '__main__':
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(solve())
