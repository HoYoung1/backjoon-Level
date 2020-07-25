# 0 ~ 9
complete_numbers = [
    "111101101101111",
    "001001001001001",
    "111001111100111",
    "111001111001111",
    "101101111001001",
    "111100111001111",
    "111100111101111",
    "111001001001001",
    "111101111101111",
    "111101111001111"
]

# for num in numbers:
#     print(num[:3])
#     print(num[3:6])
#     print(num[6:9])
#     print(num[9:12])
#     print(num[12:15])

answers_sum = 0
answers_count = 1

def get_answer(availabel_list):
    global answers_sum, answers_count

    for idx, row in enumerate(availabel_list):
        if not row:
            return -1
        answers_count *= len(row)


    for idx, row in enumerate(availabel_list):
        temp_count = answers_count / len(row)
        for num in row:
            answers_sum += (num * 10 ** (N - idx - 1)) * temp_count

    # def dfs(depth, s):
    #     global answers_sum, answers_count
    #
    #     if depth == N:
    #         answers_sum += int(s)
    #         answers_count += 1
    #         return
    #     for num in availabel_list[depth]:
    #         dfs(depth+1, s+str(num))
    # dfs(0, '')

    answer = answers_sum/answers_count
    # print()

    return answer


def solve(N, matrix):
    for idx, row in enumerate(matrix):
        matrix[idx] = matrix[idx].replace('#', '1')
        matrix[idx] = matrix[idx].replace('.', '0')

    start = 0
    end = 3

    uncomplete_numbers = []
    for i in range(N):
        one_line = ""
        for row in matrix:
            # print(one_line)
            # print(row[start:end])
            one_line += row[start:end]
        uncomplete_numbers.append(one_line)
        start += 4
        end += 4
    # print('uncomplete numbers' , uncomplete_numbers)

    availabel_list = [[] for _ in range(N)]
    # CHeck uncomplete numbers
    for idx1, uncomplete_number in enumerate(uncomplete_numbers):
        for idx2, complete_number in enumerate(complete_numbers):
            compared_value = int(uncomplete_number,2) & int(complete_number,2)
            # print()
            # print('uncomplete_number', uncomplete_number)
            # print('complete number', complete_number)
            # print('compared_value', compared_value)
            #
            if compared_value == int(uncomplete_number,2):
                availabel_list[idx1].append(idx2)
    # print('availabel_list', availabel_list)

    answer = get_answer(availabel_list)
    # print('answer', answer)
    print(answer)


if __name__ == '__main__':
    N = int(input()) # N은 9보다 작거나 같은 자연수
    matrix = [input() for _ in range(5)]

    solve(N, matrix)

