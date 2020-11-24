import sys
input = sys.stdin.readline


def get_answer(processed_words, target):
    result = 0
    for splited_target in target.split():
        if len(splited_target) == 1:
            temp = splited_target
        else:
            temp = splited_target[0] + ''.join(sorted(splited_target[1:-1])) + splited_target[-1]

        if temp in processed_words:
            if result == 0:
                result = 1
            result *= processed_words[temp]
    return result


if __name__ == '__main__':
    N = int(input().rstrip())
    words = [input().rstrip() for _ in range(N)]

    M = int(input().rstrip())
    targets = [input().rstrip() for _ in range(M)]
    
    processed_words = {}
    for word in words:
        if len(word) == 1:
            temp = word
        else:
            temp = word[0] + ''.join(sorted(word[1:-1])) + word[-1]

        if temp in processed_words:
            processed_words[temp] += 1
        else:
            processed_words[temp] = 1
    # print(processed_words)
    for target in targets:
        print(get_answer(processed_words, target))

