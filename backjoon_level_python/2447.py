def draw_star(n):
    if n == 3:
        matrix[0][:3] = [1] * 3
        matrix[1][:3] = [1, 0, 1]
        matrix[2][:3] = [1] * 3
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                matrix[a * i + k][a * j:a * (j + 1)] = matrix[k][:a]  # 핵심 아이디어


if __name__ == '__main__':
    N = int(input())

    # 메인 데이터 선언
    matrix = [[0]*N for i in range(N)]

    draw_star(N)

    for row in matrix:
        for j in row:
            if j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
