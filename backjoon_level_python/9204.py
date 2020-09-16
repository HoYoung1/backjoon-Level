alpha = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8
}

# Q 접점 어케 구했는지?
def get_tangent_point(X1, Y1, X2, Y2):
    set_A = set()
    set_B = set()

    for i in range(1, 9):
        temp_x1 = X1 + i
        temp_y1 = Y1 + i
        if 1 <= temp_x1 <= 8 and 1 <= temp_y1 <= 8:
            set_A.add((temp_x1, temp_y1))

        temp_x1 = X1 + i
        temp_y1 = Y1 - i
        if 1 <= temp_x1 <= 8 and 1 <= temp_y1 <= 8:
            set_A.add((temp_x1, temp_y1))

        temp_x1 = X1 - i
        temp_y1 = Y1 + i
        if 1 <= temp_x1 <= 8 and 1 <= temp_y1 <= 8:
            set_A.add((temp_x1, temp_y1))

        temp_x1 = X1 - i
        temp_y1 = Y1 - i
        if 1 <= temp_x1 <= 8 and 1 <= temp_y1 <= 8:
            set_A.add((temp_x1, temp_y1))

        temp_x2 = X2 + i
        temp_y2 = Y2 + i
        if 1 <= temp_x2 <= 8 and 1 <= temp_y2 <= 8:
            set_B.add((temp_x2, temp_y2))

        temp_x2 = X2 + i
        temp_y2 = Y2 - i
        if 1 <= temp_x2 <= 8 and 1 <= temp_y2 <= 8:
            set_B.add((temp_x2, temp_y2))

        temp_x2 = X2 - i
        temp_y2 = Y2 + i
        if 1 <= temp_x2 <= 8 and 1 <= temp_y2 <= 8:
            set_B.add((temp_x2, temp_y2))

        temp_x2 = X2 - i
        temp_y2 = Y2 - i
        if 1 <= temp_x2 <= 8 and 1 <= temp_y2 <= 8:
            set_B.add((temp_x2, temp_y2))

    t = set_A & set_B
    x, y = t.pop()
    return chr(ord('A') + x - 1), y


# 무조건 2번만에 갈 수 잇는거같은데..
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X1, Y1, X2, Y2 = input().split()
        X1, Y1, X2, Y2 = alpha[X1], int(Y1), alpha[X2], int(Y2)
        if X1 == X2 and Y1 == Y2:
            print('{} {} {}'.format(0, chr(ord('A') + X1 - 1), Y1))
        elif (X1+Y1) % 2 != (X2+Y2) % 2:
            print('Impossible')
        elif abs(X2-X1) == abs(Y2-Y1):
            print('1 {} {} {} {}'.format(chr(ord('A') + X1 - 1), Y1, chr(ord('A') + X2 - 1),Y2))
        else:
            print('2 {} {} {} {} {}'.format(chr(ord('A') + X1 - 1), Y1, ' '.join(map(str, get_tangent_point(X1,Y1,X2,Y2))), chr(ord('A') + X2 - 1), Y2))


