def ccw(p1, p2, p3):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    p3_x, p3_y = p3
    result = (p1_x * p2_y + p2_x * p3_y + p3_x * p1_y) - (p2_x * p1_y + p3_x * p2_y + p1_x * p3_y)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0


if __name__ == '__main__':
    A_x, A_y, B_x, B_y = list(map(int, input().split()))
    C_x, C_y, D_x, D_y = list(map(int, input().split()))

    ABC = ccw([A_x, A_y], [B_x, B_y], [C_x, C_y])
    ABD = ccw([A_x, A_y], [B_x, B_y], [D_x, D_y])
    CDA = ccw([C_x, C_y], [D_x, D_y], [A_x, A_y])
    CDB = ccw([C_x, C_y], [D_x, D_y], [B_x, B_y])

    if ABC * ABD == 0 and CDA * CDB == 0:
        a = A_x
        b = B_x
        c = C_x
        d = D_x

        if B_x < A_x:
            a = B_x
            b = A_x
        if D_x < C_x:
            c = D_x
            d = C_x
        if a <= d and c <= d:
            print(1)
        else:
            print(0)
    elif ABC * ABD <= 0 and CDA * CDB <= 0:
        print(1)
    else:
        print(0)