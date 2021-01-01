import heapq
import sys

input = sys.stdin.readline 


def solve():
    answer = 0
    count = 0

    processed_coordinates = []

    for x, y in coordinates:
        if abs(x-y) > d:
            continue
        elif x > y:
            processed_coordinates.append([y, x])
        else:
            processed_coordinates.append([x, y])

    processed_coordinates.sort(key=lambda x: x[1])
    # print(processed_coordinates)
    min_hq = []

    for x, y in processed_coordinates:
        if y-x <= d:
            count += 1
            heapq.heappush(min_hq, x)

        while min_hq:
            if min_hq[0] < y-d:
                heapq.heappop(min_hq)
                count -= 1
            else:
                break
        answer = max(answer, count)
    return answer


if __name__ == '__main__':
    n = int(input().rstrip())
    coordinates = [list(map(int, input().rstrip().split())) for _ in range(n)]
    d = int(input().rstrip())

    print(solve())