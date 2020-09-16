        import sys
        sys.setrecursionlimit(10**8)

        counter = 0
        answer = 0

        def divide(size, start_x, start_y):
            # print(size, start_x, end_x, start_y, end_y)
            global counter, answer

            if size == 2:
                if start_x == r and start_y == c:
                    answer = counter
                counter += 1

                if start_x == r and start_y+1 == c:
                    answer = counter
                counter += 1

                if start_x + 1 == r and start_y == c:
                    answer = counter
                counter += 1

                if start_x+1 == r and start_y+1 == c:
                    answer = counter
                counter += 1
                return

            next_size = size // 2

            next_x, next_y = start_x, start_y
            if next_x <= r <= next_x + next_size and next_y <= c <= next_y + next_size:
                divide(next_size, next_x, next_y)
            else:
                counter += next_size ** 2

            next_x, next_y = start_x, start_y + next_size
            if next_x <= r <= next_x + next_size and next_y <= c <= next_y + next_size:
                divide(next_size, next_x, next_y)
            else:
                counter += next_size ** 2

            next_x, next_y = start_x + next_size, start_y
            if next_x <= r <= next_x + next_size and next_y <= c <= next_y + next_size:
                divide(next_size, next_x, next_y)
            else:
                counter += next_size ** 2

            next_x, next_y = start_x + next_size, start_y + next_size
            if next_x <= r <= next_x + next_size and next_y <= c <= next_y + next_size:
                divide(next_size, next_x, next_y)
            else:
                counter += next_size ** 2


        def solve(N, r, c):
            divide(size, 0, 0)
            return answer


        if __name__ == '__main__':
            N, r, c = map(int, input().split())
            size = 2 ** N
            # matrix = [[0] * size for _ in range(size)]

            print(solve(N, r, c))


