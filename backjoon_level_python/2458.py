def print_matrix(height):
    for row in height:
        print(row)
    print()


if __name__ == '__main__':
    N, M = map(int, input().split())
    height = [[False] * (N+1) for _ in range(N+1)]
    answer = 0

    for _ in range(M):
        stu1, stu2 = map(int, input().split())
        height[stu1][stu2] = True

    # 플로이드 와샬
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if height[i][k] is True and height[k][j] is True:
                    height[i][j] = True

    # find answer
    for i in range(1, N+1):
        temp = 0
        for j in range(1, N+1):
            if height[i][j] is True:
                temp += 1
            if height[j][i] is True:
                temp += 1
        if temp == N-1:
            answer += 1
    print(answer)


