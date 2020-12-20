import sys


def get_section_num(mid):
    result = 1 # 최소 구간 1개

    min_p = max_p = numbers[0]
    for i in range(1, len(numbers)):
        min_p = min(min_p, numbers[i])
        max_p = max(max_p, numbers[i])
        if max_p-min_p > mid:
            result += 1
            min_p = numbers[i]
            max_p = numbers[i]
    return result


def solve(N, M, numbers):
    answer = sys.maxsize

    start = 0
    end = max(numbers)
    while start <= end:
        mid = (start + end) // 2
        if get_section_num(mid) <= M:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(solve(N, M, numbers))