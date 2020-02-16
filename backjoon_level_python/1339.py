def solution2(words):
    word_weights = [0] * 26  # From A to J
    for word in words:
        for idx, alpha in enumerate(word[::-1]):
            x = ord(alpha) - ord('A')
            word_weights[x] += 10**idx

    word_weights.sort(reverse=True)
    # print(word_weights)
    max_sum = 0
    for idx, weight in enumerate(word_weights):
        max_sum += weight * (9-idx)

    return max_sum


if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]

    print(solution2(words))