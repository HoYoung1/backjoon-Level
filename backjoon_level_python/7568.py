def solve(weight_heights):
    for i in range(N):
        rank = 1
        for j in range(N):
            if i == j:
                continue
            w1, h1 = weight_heights[i]
            w2, h2 = weight_heights[j]
            if w2 > w1 and h2 > h1:
                rank += 1
        print(rank, end=" ")


if __name__ == '__main__':
    N = int(input())
    weight_heights = [list(map(int, input().split())) for _ in range(N)]
    solve(weight_heights)