# https://youtu.be/xWOWwJEgiJQ?t=368

def solve(N):
    answer = 0

    value = 1
    current = 1
    limit = 1
    for i in range(1, N+1):
        answer += value
        current += 1
        if current > limit:
            current = 1
            limit += 1
            value *= 2
    return answer




if __name__ == '__main__':
    N = int(input())
    print(solve(N) % 9901)