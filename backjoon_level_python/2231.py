def solve(N):
    result = 0
    for i in range(1, N+1):
        if i + sum(map(int, list(str(i)))) == N:
            result = i
            break
    return result


if __name__ == '__main__':
    N = int(input())
    print(solve(N))