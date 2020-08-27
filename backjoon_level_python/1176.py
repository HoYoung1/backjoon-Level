import sys
sys.setrecursionlimit(10**8)


def solve(N, K, heights):
    dfs(0)
    return answer


def dfs(depth):
    global answer, temp_arr
    if depth == students_num:
        # print(temp_arr)
        answer += 1
        return
    for i in range(students_num):
        if visited[i] is False:
            # print(i)
            # print(temp_arr)
            if not temp_arr or abs(heights[i] - temp_arr[-1]) > K:
                visited[i] = True
                temp_arr.append(heights[i])
                dfs(depth+1)
                temp_arr = temp_arr[:-1]
                visited[i] = False






if __name__ == '__main__':
    N, K = map(int, input().split())
    heights = [int(input()) for i in range(N)]

    answer = 0
    students_num = len(heights)
    visited = [False] * students_num
    temp_arr = []

    print(solve(N, K, heights))