# https://www.acmicpc.net/problem/3019
# 29380KB, 64ms

block_rotate = {
    1: [[0], [0, 0, 0, 0]],
    2: [[0, 0]],
    3: [[0, 0, 1], [1, 0]],
    4: [[1, 0, 0], [0, 1]],
    5: [[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]],
    6: [[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]],
    7: [[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]
}


def solve(c, p, heights):
    answer = 0

    block = block_rotate[p]
    rotate_num = len(block)
    for i in range(rotate_num):
        for j in range(0, c - len(block[i]) + 1):
            success = True
            before_value = heights[j] - block[i][0]
            for k in range(len(block[i])):
                idx = j+k
                if before_value != heights[idx] - block[i][k]:
                    success = False
                    break
                before_value = heights[idx] - block[i][k]
            if success:
                answer += 1

    return answer


if __name__ == '__main__':
    C, P = map(int, input().split())
    heights = list(map(int, input().split()))
    print(solve(C, P, heights))
    # print(solve(6, 3, [2,1,1,1,0,1]))
