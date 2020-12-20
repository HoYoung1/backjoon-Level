def solve(numbers, targets):
    numbers.sort()
    for target in targets:
        print(binary_search(numbers, target))


def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2
        if target > numbers[mid]:
            start = mid + 1
        elif target < numbers[mid]:
            end = mid - 1
        else:
            return 1
    return 0


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))

    solve(numbers, targets)