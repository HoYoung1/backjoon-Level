import bisect
from collections import Counter

def solve(numbers, targets):
    answers = []

    numbers.sort()
    for target in targets:
        l = bisect.bisect_left(numbers, target)
        r = bisect.bisect_right(numbers, target)
        answers.append(r-l)
    return answers


if __name__ == '__main__':
    N = int(input().rstrip())
    numbers = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    targets = list(map(int, input().rstrip().split()))

    print(' '.join(map(str, solve(numbers, targets))))
