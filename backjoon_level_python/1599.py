from functools import cmp_to_key
import sys
input = sys.stdin.readline


def compare(string1, string2):
    # 두 스트링중에 누가 더 작은지
    order = 'abkdeghilmn+oprstuwy'
    i = 0
    while True:
        if i == len(string1) or i == len(string2):
            if len(string1) < len(string2):
                return -1
            elif len(string1) == len(string2):
                return 0
            else:
                return 1

        order_index_string1 = order.index(string1[i])
        order_index_string2 = order.index(string2[i])

        if order_index_string1 < order_index_string2:
            return -1
        elif order_index_string1 > order_index_string2:
            return 1
        else:
            i += 1


def solve(queries):
    list_queries = []
    for query in queries:
        converted_text = convert_list_from_text(query)
        # print('converted_text', converted_text)

        list_queries.append(converted_text)

    for i in range(len(list_queries)):
        list_queries[i] = ''.join(list_queries[i])

    # print('list_quires', list_queries)
    list_queries.sort(key=cmp_to_key(compare))
    # print(list_queries)

    for query in list_queries:
        print(query.replace('+', 'ng'))



def convert_list_from_text(text):
    temp = []

    # + 는 ng를의미 -는 pass하라는걸의미
    text_list = list(text)
    for i in range(len(text_list)):
        if i != len(text) - 1 and text_list[i] == 'n' and text_list[i + 1] == 'g':
            temp.append('+')
            text_list[i + 1] = '-'
        elif text_list[i] == '-':
            continue
        else:
            temp.append(text_list[i])
    return temp


if __name__ == '__main__':
    N = int(input())
    queries = []
    for i in range(N):
        queries.append(input().rstrip())
    solve(queries)

    # print(compare('abkk','abk'))
