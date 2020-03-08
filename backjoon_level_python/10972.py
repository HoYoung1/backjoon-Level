def find_next_permutation(permutation):
    if permutation == [1]:
        return [-1]
    i = -1
    j = -1
    n = len(permutation) - 1
    for idx in range(0,n):
        # find i
        if permutation[idx] < permutation[idx+1]:
            i = idx
    if i == -1:
        return [-1]  # 마지막 순열

    for idx in range(n, i, -1):
        # find j
        if permutation[idx] > permutation[i]:
            j = idx
            break

    permutation[i], permutation[j] = permutation[j], permutation[i]
    # print(permutation[:i])
    # print(list(reversed(permutation[i:])))
    return permutation[:i+1] + list(reversed(permutation[i+1:]))


def solution(permutation):
    next_permutation = find_next_permutation(permutation)
    return next_permutation


if __name__ == '__main__':
    N = int(input())
    permutation = list(map(int, input().split()))
    next_permutation = solution(permutation)
    for idx, num in enumerate(next_permutation):
        print(num, end=' ')

