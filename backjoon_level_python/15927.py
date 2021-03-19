def is_all_same_alpha():
    before = s[0]
    for k in s[1:]:
        if before != k:
            return False
        before = k
    return True


def solve(s):
    if s != s[::-1]:
        return len(s)
    else:
        if is_all_same_alpha():
            return -1
        else:
            return len(s)-1


if __name__ == '__main__':
    s = input()
    print(solve(s))