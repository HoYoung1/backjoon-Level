def dfs(current_sum, target_sum):
    global sum_count

    for i in range(1, 4):
        if current_sum > target_sum:
            return
        elif current_sum == target_sum:
            sum_count += 1
            return
        else:
            dfs(current_sum+i, target_sum)


def solution(n):
    start = 0
    dfs(start, n)
    return sum_count


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sum_count = 0
        print(solution(int(input())))
