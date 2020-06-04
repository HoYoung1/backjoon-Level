def solve(N, mans, womans):
    answer = 0
    mans.sort()
    womans.sort(reverse=True)

    man_pointer = 0
    woman_pointer = 0
    while man_pointer < N and woman_pointer < N:
        if mans[man_pointer] < 0 and womans[woman_pointer] < 0:
            man_pointer += 1
        elif mans[man_pointer] > 0 and womans[woman_pointer] > 0:
            woman_pointer += 1
        elif womans[woman_pointer] > 0 and womans[woman_pointer] >= abs(mans[man_pointer]):
            woman_pointer += 1
        elif womans[woman_pointer] < 0 and abs(womans[woman_pointer]) <= (mans[man_pointer]):
            woman_pointer += 1
        else:
            answer += 1
            woman_pointer += 1
            man_pointer += 1
    return answer


if __name__ == '__main__':
    N = int(input())
    mans = list(map(int, input().split()))
    womans = list(map(int, input().split()))
    print(solve(N, mans, womans))

