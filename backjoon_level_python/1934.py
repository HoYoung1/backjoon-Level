def gcd(a, b):
    # 재귀
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


if __name__ == '__main__':
    # print(gcd(15, 5))
    for i in range(int(input())):
        A, B = map(int, input().split())
        print(lcm(A, B))

# 참고 https://blockdmask.tistory.com/53
