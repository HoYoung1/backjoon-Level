def solution(M, N, x, y):
    maximum = M * N
    count = x
    answer = -1
    while count <= maximum:
        val = count % N
        if (val == 0 and y == N) or (val == y):
            answer = count
            break
        count += M
    return answer


if __name__ == '__main__':
    for _ in range(int(input())):
        M, N, x, y = map(int, input().split())
        print(solution(M, N, x, y))
