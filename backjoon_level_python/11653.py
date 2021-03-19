def solve(N):
    result = []

    target = N
    while target != 1:
        for i in range(2, target + 1):
            if target % i == 0:
                result.append(i)
                target //= i
                break
    return result


if __name__ == '__main__':
    N = int(input())
    for num in solve(N):
        print(num)