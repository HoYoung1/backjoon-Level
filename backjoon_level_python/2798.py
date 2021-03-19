def solve(N, M, numbers):
    result = 0

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                sum_of_card = numbers[i] + numbers[j] + numbers[k]
                if sum_of_card <= M:
                    result = sum_of_card
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solve(N, M, numbers))