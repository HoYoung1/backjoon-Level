def solve(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    print(solve(x, y))