answer = 0


# 29380KB, 728ms
# def dfs1(depth, before_sum, before_idx):
#     global answer
#
#     if depth != 0 and before_sum == S:
#         answer += 1
#
#     for idx in range(before_idx, N):
#         if visited[idx] is False:
#             visited[idx] = True
#             dfs(depth + 1, before_sum + numbers[idx], idx+1)
#             visited[idx] = False

# 29380KB, 516ms
def dfs2(i, current_sum):
    global answer

    if i == N:
        return
    if current_sum + numbers[i] == S:
        answer += 1
    dfs2(i+1, current_sum)
    dfs2(i+1, current_sum + numbers[i])


def solve():
    # dfs1(0, 0, 0)
    dfs2(0, 0)
    return answer


if __name__ == '__main__':
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    visited = [False] * N

    print(solve())