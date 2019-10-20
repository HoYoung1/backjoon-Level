# def find_fraction(n):
#     left_num = 1
#     right_num = 1
#     direction = -1
#
#     for i in range(1, n):
#         right_num -= direction
#         left_num += direction
#         if left_num == 0 or right_num == 0:
#             direction *= -1
#             if direction == 1:
#                 left_num += 1
#             elif direction == -1:
#                 right_num += 1
#     return left_num, right_num


# def find_fraction(n):
#     left_num = 1
#     right_num = 2
#     cal = 1
#     if n == 1:
#         return 1, 1
#     for i in range(2, n):
#         left_num += cal
#         right_num += cal * -1
#
#         if left_num == 0:
#             left_num = 1
#             cal *= -1
#         elif right_num == 0:
#             right_num = 1
#             cal *= -1
#     return left_num, right_num

# 시간초과
# def find_fraction(n):
#     add = 1
#     while n > add:
#         n = n - add
#         add += 1
#     a = n
#     b = add - n + 1
#     if add % 2 == 1:
#         a, b = b, a
#     return str(a) + "/" + str(b)

def find_fraction(n):
    i = 1
    deleting_n = n
    while deleting_n > i:
        deleting_n -= i
        i += 1
    cnt_in_pos = deleting_n - 1
    a = 1 + cnt_in_pos
    b = i - cnt_in_pos

    if i % 2 != 0:
        a, b = b, a
    return a, b


if __name__ == '__main__':
    a, b = find_fraction(int(input()))
    print(str(a) + "/" + str(b))


def test_find_fraction():
    assert find_fraction(14) == (2, 4)
