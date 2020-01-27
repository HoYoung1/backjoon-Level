# 시간초과
def solution1(N):
    sum = 0
    for i in range(1, N+1):
        sum += len(str(i))
    return sum

# 시간초과
def solution2(N):
    sum = ""
    for i in range(1, N+1):
        sum += str(i)
    return len(sum)


# 풀이방법 : https://www.acmicpc.net/board/view/23735 참고
def solution3(N):
    sum = 0
    i = 1
    while True:
        if i > N:
            break
        else:
            sum += N - i + 1
            i *= 10
    return sum


if __name__ == '__main__':
    N = int(input())
    print(solution3(N))
