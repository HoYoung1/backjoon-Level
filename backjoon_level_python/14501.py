#https://www.acmicpc.net/problem/14501
#29380KB 84ms

maximum_pay = 0


def dfs(tp, current_idx, current_sum):
    global maximum_pay

    if current_idx > N:
        return

    maximum_pay = max(maximum_pay, current_sum)

    if current_idx == N:
        return

    dfs(tp, current_idx + tp[current_idx][0], current_sum+tp[current_idx][1])
    dfs(tp, current_idx + 1, current_sum)




def solve(tp):
    dfs(tp, 0, 0)
    return maximum_pay


if __name__ == '__main__':
    N = int(input())
    TP = []
    for _ in range(N):
        TP.append(list(map(int, input().split())))
    print(solve(TP))