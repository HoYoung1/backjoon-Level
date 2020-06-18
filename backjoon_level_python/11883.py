from collections import deque


# def get_sum(string):
#     result = 0
#     for c in string:
#         result += int(c)
#     return result

success = None
answer = None
# def solve(birth_number_sum):
#     global success
#     global answer
#
#     answer = -1
#     success = False
#
#     def dfs(current):
#         global success
#         global answer
#
#         s = get_sum(current)
#         if s > birth_number_sum:
#             # backtrack
#             return
#         if s == birth_number_sum:
#             success = True
#             answer = current
#         if success:
#             return
#         for i in ['3', '5', '8']:
#             dfs(current + i)
#
#     dfs('')
#     return answer





# def solve2(birth_number_sum):
#     birth_nums = ['3', '5', '8']
#     dq = deque()
#     for num in birth_nums:
#         dq.append(num)
#     while dq:
#         check_num = dq.popleft()
#         if get_sum(check_num) == birth_number_sum:
#             return check_num
#         elif get_sum(check_num) > birth_number_sum:
#             continue
#         else:
#             for num in birth_nums:
#                 dq.append(check_num + num)
#     return -1

def solve3(birth_number_sum):
    birth_nums = ['3', '5', '8']
    dq = deque()
    for num in birth_nums:
        dq.append((num, int(num)))
    while dq:
        check_num, current_sum = dq.popleft()
        for num in birth_nums:
            if current_sum + int(num) == birth_number_sum:
                return check_num + num
            elif current_sum + int(num) < birth_number_sum:
                dq.append((check_num + num, current_sum + int(num)))
    return -1


def solve4(birth_number_sum):
    digit_num = get_digit_num(birth_number_sum)
    if digit_num == -1:
        return -1

    for i in range(digit_num, -1, -1):
        g_i = i
        g_j = 0
        g_k = 0

        for j in range(digit_num-i, -1, -1 ):
            # print(digit_num-i)
            g_j = j
            # for k in range(digit_num-i-j, 0, -1):
            #     g_j = k
            #     print(digit_num-i-j)
            #     print()
            g_k = digit_num - i - j
            if 3 * g_i + 5 * g_j + 8 * g_k == birth_number_sum:
                return '3' * g_i + '5' * g_j + '8' * g_k
        if i == digit_num and 3 * g_i + 5 * g_j + 8 * g_k == birth_number_sum:
            return '3'*g_i + '5'*g_j + '8'*g_k



def get_digit_num(birth_number_sum):
    birth_nums = ['3', '5', '8']
    dq = deque()
    for num in birth_nums:
        dq.append((1, int(num)))
    while dq:
        digit_num, current_sum = dq.popleft()
        for num in birth_nums:
            if current_sum + int(num) == birth_number_sum:
                return digit_num+1
            elif current_sum + int(num) < birth_number_sum:
                dq.append((digit_num + 1, current_sum + int(num)))
    return -1


def solve5():
    def get_num_from_digit(birth_number_sum, digit_num):
        for i in range(digit_num, -1, -1):
            g_i = i
            g_j = 0
            g_k = 0

            for j in range(digit_num - i, -1, -1):
                # print(digit_num-i)
                g_j = j
                # for k in range(digit_num-i-j, 0, -1):
                #     g_j = k
                #     print(digit_num-i-j)
                #     print()
                g_k = digit_num - i - j
                if 3 * g_i + 5 * g_j + 8 * g_k == birth_number_sum:
                    return '3' * g_i + '5' * g_j + '8' * g_k
            if i == digit_num and 3 * g_i + 5 * g_j + 8 * g_k == birth_number_sum:
                return '3' * g_i + '5' * g_j + '8' * g_k


    def get_num_from_digit2(birth_number_sum, digit_num):
        result = ''
        dq = deque()
        dq.append((birth_number_sum, digit_num))
        while dq:
            here, cnt = dq.popleft()
            if here == 0:
                break
            for i in ['3', '5', '8']:
                next = here - int(i)
                if next < 0:
                    continue
                if minimum_digits[next] == cnt - 1:
                    dq.append((next, cnt-1))
                    result += i
                    break
        return result

    minimum_digits = [-1] * 1000001
    minimum_digits[0] = 0

    birth_nums = ['3', '5', '8']
    dq = deque()
    dq.append((0, ''))
    while dq:
        current_sum, checknum = dq.popleft()
        digit_num = len(checknum)
        for num in birth_nums:
            next_num_type_string = checknum + num
            next_sum = current_sum + int(num)
            if int(next_sum) < 1000001 and minimum_digits[next_sum] == -1:
                minimum_digits[int(next_sum)] = digit_num + 1
                dq.append((next_sum, next_num_type_string))

    for _ in range(int(input())):
        a = int(input())
        digit_num = minimum_digits[a]
        if digit_num == -1:
            print(-1)
        else:
            print(get_num_from_digit2(a, digit_num))


if __name__ == '__main__':
    # T = int(input())
    # for _ in range(T):
    #     birth_number_sum = int(input())
    #     print(solve5(birth_number_sum))
    solve5()


