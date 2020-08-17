def get_score(text):
    text = text.replace(' ', '')
    return eval(text)


def dfs(depth, number_with_sign):
    number_with_sign += str(depth)
    if depth == N:
        if get_score(number_with_sign) == 0:
            print(number_with_sign)
        return

    dfs(depth + 1, number_with_sign + ' ')
    dfs(depth + 1, number_with_sign + '+')
    dfs(depth + 1, number_with_sign + '-')


if __name__ == '__main__':
    T = int(input())
    signs = ['+', '-', ' ']
    for _ in range(T):
        N = int(input())
        dfs(1, '')
        print()

    # assert get_score('1+2-3+4-5-6+7') == 0
    # assert get_score('1+2-3') == 0
    # assert get_score('1-2 3-4 5+6 7') == 0

