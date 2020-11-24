import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input().rstrip())
    in_cars = {input().rstrip():i for i in range(n)}
    out_cars = [in_cars[input().rstrip()] for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            if out_cars[i] > out_cars[j]:
                answer += 1
                break
    print(answer)


