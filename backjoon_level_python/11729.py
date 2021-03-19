

def solve(N):
    result = []

    def hanoi(cnt, start, target, assitant):
        if cnt == 1:
            result.append((start, target))
            return
        hanoi(cnt - 1, start, assitant, target)
        result.append((start, target))
        hanoi(cnt - 1, assitant, target, start)
    hanoi(N, 1, 3, 2)

    return result


if __name__ == '__main__':
    N = int(input())
    answer = solve(N)
    print(len(answer))
    for s, e in answer:
        print(s, e)