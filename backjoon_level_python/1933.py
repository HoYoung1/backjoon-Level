# 런타임에러
# 배열을 사이즈가 너무 큼. 10억이면 4byte만해도 4000MB임 파이썬은 4byte보다 큼..
def solve():
    #heights = [0] * 1000000000
    heights = [0] * 100000
    result = ''
    for i in range(N):
        L, H, R = map(int, input().split())
        for j in range(L, R):
            if heights[j] < H:
                heights[j] = H
    for i in range(len(heights) - 1):
        if heights[i] != heights[i + 1]:
            result += '{} {} '.format(i + 1, heights[i + 1])
    return result


if __name__ == '__main__':
    N = int(input())
    print(solve())
