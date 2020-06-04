#29380KB 64ms
def solve(N):
    decreasing_numbers = []

    def dfs(num):
        decreasing_numbers.append(num)
        last_digit = num % 10
        for i in range(last_digit - 1, -1, -1):
            dfs(num * 10 + i)

    for i in range(0, 10):
        dfs(i)

    decreasing_numbers.sort()

    if N >= len(decreasing_numbers):
        return -1
    return decreasing_numbers[N]


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
