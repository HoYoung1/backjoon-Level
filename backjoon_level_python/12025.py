def solve(password, k):
    answer = ''
    bit = bin(k-1)[2:]
    bit = ''.join(reversed(bit))
    # print('bit', bit)
    count = 0

    password = password.replace('6', '1').replace('7','2')

    for s in password[::-1]:
        if count < len(bit):
            if s == '1':
                if bit[count] == '1':
                    answer += '6'
                else:
                    answer += s
                count += 1
            elif s == '2':
                if bit[count] == '1':
                    answer += '7'
                else:
                    answer += s
                count += 1
            else:
                answer += s
        else:
            answer += s
    # print(count)
    # print(''.join(reversed(answer)))
    if count == len(bit):
        return ''.join(reversed(answer))
    else:
        return -1



if __name__ == '__main__':
    password = input()
    k = int(input())
    print(solve(password, k))