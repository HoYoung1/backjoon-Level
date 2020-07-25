if __name__ == '__main__':
    N = int(input())  # N은 200이하이다.
    M = int(input()) # M은 1000이하이다.

    matrix = [list(map(int, input().split())) for _ in range(N)]

    path = list(map(int, input().split()))

    # print(matrix)

    # print(matrix)
    #floyd warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
    # print(matrix)

    for i in range(len(path)-1):
        idx = path[i] -1
        next_idx = path[i+1] -1
        if matrix[idx][next_idx] == 0 and idx != next_idx:
            print('NO')
            break
    else:
        print('YES')

