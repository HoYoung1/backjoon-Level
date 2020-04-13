# https://www.acmicpc.net/problem/1062
# pypy3
# 142048KB 1028ms

def dfs(depth, spells, idx):
    global max_count

    if depth == K:
        count = get_readable_word_count()
        max_count = max(max_count, count)
        return

    for i in range(idx, len(spells)):
        if not visited[i]:
            visited[i] = True
            alpha[ord(spells[i]) - Ord_a] = True
            dfs(depth+1, spells, i+1)
            alpha[ord(spells[i]) - Ord_a] = False
            visited[i] = False


def get_readable_word_count():
    readable_word_count = 0
    for word in words:
        success = True
        for c in word:
            if not alpha[ord(c) - Ord_a]:
                success = False
                break
        if success is True:
            readable_word_count += 1
    return readable_word_count


def solve():
    global K

    if len(spells) < K:
        K = len(spells)

    dfs(0, list(spells), 0)
    return max_count


if __name__ == '__main__':
    GIVEN_SPELLINGS = ['a', 'c', 'n', 't', 'i']
    alpha = [False] * 26
    Ord_a = ord('a')  # 97
    max_count = 0

    for spelling in GIVEN_SPELLINGS:
        alpha[ord(spelling) - Ord_a] = True

    # 첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다.
    N, K = map(int, input().split())
    K -= len(GIVEN_SPELLINGS)

    words = [input()[4:-4] for _ in range(N)]

    spells = set()
    for word in words:
        for c in word:
            spells.add(c)

    spells -= set(GIVEN_SPELLINGS)
    visited = [False] * len(spells)

    max_count = solve()
    print(max_count)


# 3 6
# antarctica
# antahellotica
# antacartica

# 1 5
# antatica
