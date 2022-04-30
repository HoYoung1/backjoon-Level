def solve(a, b, c):
    result = max(a, b, c) * 100
    if a == b == c:
        result = 10000 + a * 1000
    elif a == b:
        result = 1000 + a * 100
    elif b == c:
        result = 1000 + b * 100
    elif a == c:
        result = 1000 + a * 100
    return result


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

