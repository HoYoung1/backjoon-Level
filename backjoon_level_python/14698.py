import heapq
import sys

input = sys.stdin.readline


if __name__ == '__main__':

    T = int(input().rstrip())
    for _ in range(T):
        _ = input().rstrip()
        numbers = list(map(int, input().rstrip().split()))

        answer = 1
        heapq.heapify(numbers)
        while len(numbers) != 1:
            num1 = heapq.heappop(numbers)
            num2 = heapq.heappop(numbers)
            new_num = num1 * num2

            heapq.heappush(numbers, new_num)
            answer *= new_num
        print(answer % 1000000007)






