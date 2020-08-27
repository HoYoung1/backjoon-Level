# 1. 주어진 알파벳 갯수로 만들 수 있는 부분 문자열을 추려낸다.

# 2. 조건대로 하면서 set에 넣는다.

from copy import deepcopy


# 점프 할 구간을 알 수 있어서, 더 빠르게 구현도 가능 할 듯
def get_substring(word, alphas):
    result = set()

    def get_alpha_num(alphas):
        total_num = 0
        for alpha in alphas:
            total_num += alphas[alpha]
        return total_num

    def is_valid(text, alpha_dic):
        # text가 알파벳갯수랑 딱 맞아야 True
        temp_dic = deepcopy(alpha_dic)
        for t in text:
            if t in temp_dic.keys() and temp_dic[t] > 0:
                temp_dic[t] -= 1
            else:
                return False

        for t in temp_dic:
            if temp_dic[t] != 0:
                return False
        return True


    total_alpha_num = get_alpha_num(alphas)

    for i in range(len(word) - total_alpha_num + 1):
        if is_valid(word[i:i+total_alpha_num], alphas):
            result.add(word[i:i+total_alpha_num])
    return result


def list_to_dict(list):
    result = {}
    for i in range(len(list)):
        if i % 2 == 0:
            result[list[i]] = int(list[i + 1])
    return result


# Q. 어떤식으로 서브스트링을 담아야 좋은 방법인지 ...
def get_set_from_substring(substring):
    result = set()

    def dfs(word, start_idx, end_idx):
        if end_idx - start_idx == 1:
            result.add(word)
            return

        if (start_idx + end_idx) % 2 == 0:
            half_idx = (start_idx + end_idx)//2

            dfs(word[:start_idx] + word[start_idx:half_idx][::-1] + word[half_idx:end_idx] + word[end_idx:], half_idx, end_idx)
            dfs(word[:start_idx] + word[start_idx:half_idx] + word[half_idx:end_idx][::-1] + word[end_idx:], start_idx, half_idx)
        else:
            half_idx = (start_idx + end_idx) // 2
            dfs(word[:start_idx] + word[start_idx:half_idx][::-1] + word[half_idx:end_idx] + word[end_idx:], half_idx, end_idx)
            dfs(word[:start_idx] + word[start_idx:half_idx] + word[half_idx:end_idx][::-1] + word[end_idx:], start_idx, half_idx)

            half_idx = (start_idx + end_idx) // 2 + 1
            dfs(word[:start_idx] + word[start_idx:half_idx][::-1] + word[half_idx:end_idx] + word[end_idx:], half_idx, end_idx)
            dfs(word[:start_idx] + word[start_idx:half_idx] + word[half_idx:end_idx][::-1] + word[end_idx:], start_idx, half_idx)

    dfs(substring, 0, len(substring))
    return result


def solve(N, alpha_numbers, word):
    answers = set()

    alphas = list_to_dict(alpha_numbers)
    substrings = get_substring(word, alphas)
    for substring in substrings:
        answers = answers | get_set_from_substring(substring)

    return len(answers)


if __name__ == '__main__':
    N = int(input())
    alpha_numbers = input().split()
    word = input()

    print(solve(N, alpha_numbers, word))

    temp_dict = {
        'c': 1,
        'e': 2,
        'i': 1,
        'n': 2
    }
    assert list_to_dict('c 1 e 2 i 1 n 2'.split()) == temp_dict
    assert get_substring('inconvenience', temp_dict) == {'enienc', 'nience'}
    assert get_set_from_substring('enienc') | get_set_from_substring('nience') == set('eincne, einnce, einnec, enicne, ineecn, ineenc, inenec, neicne, neiecn, nieecn'.split(', '))
