def solve(N, P, S):
    answer = 0

    init = [i % 3 for i in range(N)]
    current = [i % 3 for i in range(N)]

    answer_P = [-1] * N
    for i in range(N):
        temp_i = i % 3
        temp_v = i // 3
        # answer_P[P[i]+3*temp_v] = temp_i
        cnt = 0
        while True:
            if answer_P[P[i] + 3 * cnt] == -1:
                answer_P[P[i] + 3 * cnt] = temp_i
                break
            else:
                cnt += 1
    print('answer_P', answer_P)
    while True:
        if current == answer_P:
            break
        if answer != 0 and init == current:
            print('종료')
            print('init', init)
            print('current',current)
            answer = -1
            break

        copy = [-1] * N
        for i in range(N):
            idx = S[i]
            copy[idx] = current[i]
        print('copy', copy)
        current = copy


        print('answer', answer)

        answer += 1
    return answer


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))

    print(solve(N, P, S))