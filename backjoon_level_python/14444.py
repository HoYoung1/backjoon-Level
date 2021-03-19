import sys


input = sys.stdin.readline


def expand(left: int, right: int) -> str:
    while left >= 0 and right <= len(S) and S[left] == S[right - 1]:
        left -= 1
        right += 1
    return S[left + 1:right - 1]


def solve(s):
    if len(s) <= 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result


if __name__ == '__main__':
    S = input().rstrip()
    print(len(solve(S)))