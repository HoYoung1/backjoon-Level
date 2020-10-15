import heapq
import sys
input = sys.stdin.readline

def solve(N, matrix):
    max_answer = 0
    answer = 0
    q = []
    matrix.sort(key=lambda x: x[1])

    for _, start, end in matrix:
        answer += 1
        heapq.heappush(q, end)
        while q and start >= q[0]:
            answer -= 1
            heapq.heappop(q)
        max_answer = max(max_answer, answer)

    return max_answer


if __name__ == '__main__':
    N = int(input().rstrip())
    matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

    print(solve(N, matrix))