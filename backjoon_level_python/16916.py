def get_failure_array(pattern):
    failure = [0]

    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure

def kmp(pattern, text):
    failure = get_failure_array(pattern)

    i, j = 0, 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return True
            j += 1
        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return False

if __name__ == '__main__':
    S = input()
    P = input()

    if kmp(P, S):
        print(1)
    else:
        print(0)

