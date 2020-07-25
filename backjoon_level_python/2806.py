def solve(N, DNA):

    A_num, B_num = get_AB_num(N, DNA)
    answer = min(A_num + 1, B_num)

    'ABBA'
    pointer = 0
    accumulation = 0
    while pointer+1 < N and accumulation < answer:
        if DNA[pointer] != DNA[pointer+1]:
            accumulation += 1
            if DNA[pointer] == 'B':
                a, b = get_AB_num(N-pointer-1, DNA[pointer+1:])
                sub_answer = min(a+1, b)
                answer = min(answer, accumulation+sub_answer)
                # print('뒤집기중 answer', answer)
        pointer += 1
    # print('누적', accumulation)

    if accumulation < answer:
        if DNA[-1] == 'B':
            accumulation += 1
    answer = accumulation
    return answer


def get_AB_num(N, DNA):
    A_num = DNA.count('A')
    B_num = N - A_num
    return A_num, B_num


if __name__ == '__main__':
    N = int(input())
    DNA = input()

    print(solve(N, DNA))

    # tc = 'BBABB'
    # assert solve(len(tc), tc) == 2
    #
    # tc = 'A'
    # assert solve(len(tc), tc) == 0
    #
    # tc = 'ABA'
    # assert solve(len(tc), tc) == 1
    #
    # tc = 'BBBAAABBBAAABABA'
    # assert solve(len(tc), tc) == 5
    #
    # tc = 'AAAAAABBBBBBBBBAAAAAABBBBBB'
    # assert solve(len(tc), tc) == 4



