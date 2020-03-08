import sys


def solution(permutation):
    i = -1

    # find i
    n = len(permutation) -1
    for idx in range(0, n):
        if permutation[idx] > permutation[idx+1]:
            i = idx

    # last
    if i == -1:
        return [-1]

    # find j
    for idx in range(n, i, -1):
        if permutation[i] > permutation[idx]:
            j = idx
            break
    # swap
    permutation[i], permutation[j] = permutation[j], permutation[i]

    return permutation[:i+1] + list(reversed(permutation[i+1:]))


if __name__ == '__main__':
    N = int(input())
    permutation = list(map(int, input().split()))
    answer = solution(permutation)
    for i in answer:
        print(i, end=" ")
