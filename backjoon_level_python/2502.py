if __name__ == '__main__':
    D, K = map(int, input().split())
    bb_x, bb_y = 1, 0
    b_x, b_y = 0,1
    for _ in range(3, D+1):
        x, y = bb_x + b_x, bb_y + b_y
        bb_x, bb_y = b_x, b_y
        b_x, b_y = x, y

    for i in range(K//y, 0,-1):
        remainder = K - i * y
        if remainder % x == 0:
                print(remainder // x)
                print(i)
            break
