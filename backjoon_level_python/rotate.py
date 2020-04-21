def rotate(N, matrix):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = matrix[j][N-i-1]
    return result