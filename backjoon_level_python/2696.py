import heapq

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        M = int(input())
        print(M//2 + 1)
        input_count = M // 10 + 1
        numbers = []
        for j in range(input_count):
            numbers += map(int, input().split())
        # print(numbers)

        min_h = []
        max_h = []
        middle = numbers[0]
        print(middle, end=" ")
        for j in range(1, M):
            # print('current middle, num[j]', middle,numbers[j])
            if numbers[j] < middle:
                # print('max_h push')
                heapq.heappush(max_h, numbers[j] * -1)
            else:
                # print('min_h push')
                heapq.heappush(min_h, numbers[j])

            if j % 2 == 0:
                if len(max_h) < len(min_h):
                    heapq.heappush(max_h, middle * -1)
                    middle = heapq.heappop(min_h)
                    # print('min h pop',middle)
                elif len(max_h) > len(min_h):
                    heapq.heappush(min_h, middle)
                    middle = heapq.heappop(max_h) * -1
                    # print('max h pop',middle)
                else:
                    # 같을 때
                    heapq.heappush(min_h, middle)
                    middle = heapq.heappop(min_h)
                    # print('min h pop same', middle)
                if j % 20 == 0:
                    print()
                print(middle, end=" ")

        print()


        
