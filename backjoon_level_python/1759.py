from collections import deque

dq = deque()
answers = []


def is_valid(dq):
    """
    최소 하나의 모음, 최소 두 개의 자음을 가져야함.
    """
    num_vowel = 0

    alphabets = list(dq)
    for alpha in alphabets:
        if alpha in ['a', 'e', 'i', 'o', 'u']:
            num_vowel += 1

    num_consonant = len(alphabets) - num_vowel

    if num_vowel == 0 or num_consonant < 2:
        return False
    return True


def dfs(depth, current_idx):
    if depth == L:
        if is_valid(dq):
            answers.append(list(dq))
        return

    for i in range(current_idx, len(alphas)):
        if visited[i] is False:
            visited[i] = True
            dq.append(alphas[i])

            dfs(depth + 1, i+1)

            dq.pop()
            visited[i] = False


def solve(L, C, alphas):
    alphas.sort()

    dfs(0, 0)


if __name__ == '__main__':
    L, C = map(int, input().split())
    alphas = input().split()
    visited = [False] * len(alphas)

    answer = solve(L, C, alphas)

    for answer in answers:
        print(''.join(answer))