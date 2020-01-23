
"""
최소공배수 LCM(Least Common Multiple)
최대공약수 GCD(Greatest Common Divisor)
최소공배수는 a와 b의 곱에 최대공약수를 나누어 준 것과 같다.
"""


def lcm2(a, b):
    # 유클리드 호제법

    # a % b 가 0 이라면 b가 최대공약수이다.
    # 그 렇지 않다면, b를 a에, a % b 를 b에 넣는다.
    while True:
        n = a % b
        if n == 0:
            return b

        a = b
        b = n


def gcd(a, b):
    return a * b // lcm2(a, b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd = gcd(a, b)
    print(lcm2(a, b))
    print(a*b // lcm2(a, b))
