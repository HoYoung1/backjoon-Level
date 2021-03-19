def solve(x, y, w, h):
    return min(x, y, w-x, h-y)


if __name__ == '__main__':
    x, y, w, h = list(map(int, input().split()))
    print(solve(x, y, w, h))
