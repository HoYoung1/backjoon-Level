import sys
input = sys.stdin.readline


def solve(phone_numbers):
    for i in range(len(phone_numbers)):
        for j in range(i + 1, len(phone_numbers)):
            if phone_numbers[i] == phone_numbers[j][:len(phone_numbers[i])]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        phone_numbers = [input().strip() for _ in range(n)]
        phone_numbers.sort(key=lambda p: len(p))

        print(solve(phone_numbers))


            
        
        
        
            

