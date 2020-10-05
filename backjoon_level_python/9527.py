def solve(A, B):
    result = 0
    i = 2
    while i//2 <= B:
        result += (B+1) // i * (i // 2) + max(0, (B + 1) % i - i // 2)
        result -= A // i * (i // 2) + max(0, A % i - i // 2)
        i <<= 1
    return result



if __name__ == '__main__':
    A, B = map(int, input().split())
    print(solve(A, B))