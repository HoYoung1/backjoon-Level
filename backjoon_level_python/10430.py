# '나머지' 영어로 remainder
def remainder(a, b, c):
    return (a + b) % c,\
           ((a % c) + (b % c)) % c,\
           (a * b) % c,\
           ((a % c) * (b % c)) % c


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    for i in remainder(A, B, C):
        print(i)
