

class Dice:
    def __init__(self, N, M, x, y):
        self.dice = 0
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.front = 0
        self.back = 0

        self.x = x
        self.y = y

        self.N = N
        self.M = M

        self.dx = [0, 0, 0, -1, 1]
        self.dy = [0, 1, -1, 0, 0]

    def move(self, order):
        # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로
        if order == 1:
            temp = self.down
            self.down = self.right
            self.right = self.up
            self.up = self.left
            self.left = temp

        elif order == 2:
            temp = self.down
            self.down = self.left
            self.left = self.up
            self.up = self.right
            self.right = temp

        elif order == 3:
            temp = self.down
            self.down = self.front
            self.front = self.up
            self.up = self.back
            self.back = temp

        elif order == 4:
            temp = self.down
            self.down = self.back
            self.back = self.up
            self.up = self.front
            self.front = temp

        self.x = self.x + self.dx[order]
        self.y = self.y + self.dy[order]

    def available_direction(self, order):
        temp_x = self.x + self.dx[order]
        temp_y = self.y + self.dy[order]
        if (0 <= temp_x < self.N) and (0 <= temp_y < self.M):
            return True
        return False

    def get_down_num(self):
        return self.down

    def set_down_num(self, num):
        self.down = num

    def get_up_num(self):
        return self.up


if __name__ == '__main__':
    # 첫째 줄에 지도의 세로 크기 N,
    # 가로 크기 M (1 ≤ N, M ≤ 20),
    # 주사위를 놓은 곳의 좌표 x y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1),
    # 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.
    N, M, x, y, K = list(map(int, input().split()))

    # 둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로,
    # 각 줄은 서쪽부터 동쪽 순서대로 주어진다.
    # 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다.
    # 지도의 각 칸에 쓰여 있는 수는 10을 넘지 않는 자연수 또는 0이다.
    my_map = []
    for i in range(N):
        my_map.append(list(map(int, input().split())))

    # for i in range(N):
    #     for j in range(M):
    #         print(i,j, my_map[i][j])

    # 마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
    orders = list(map(int, input().split()))

    dice = Dice(N, M, x, y)

    for order in orders:
        if dice.available_direction(order):
            dice.move(order)
            if my_map[dice.x][dice.y] == 0:
                my_map[dice.x][dice.y] = dice.get_down_num()
            else:
                dice.set_down_num(my_map[dice.x][dice.y])
                my_map[dice.x][dice.y] = 0
            print(dice.get_up_num())




