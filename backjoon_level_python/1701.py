def get_failure_array(text):
    failure = [0] * len(text)

    j = 0
    for i in range(1, len(text)):
        while j > 0 and text[i] != text[j]:
            j = failure[j - 1]
        if text[i] == text[j]:
            failure[i] = j + 1
            j += 1
    return failure


def solve(input_text):
    max_value = 0

    for i in range(len(input_text)-1):
        failure = get_failure_array(input_text[i:])
        max_value = max(max_value, max(failure))
    return max_value


if __name__ == '__main__':
    input_text = input()
    print(solve(input_text))
