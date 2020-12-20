import sys
input = sys.stdin.readline


def solve(N, M, tree_heights):
    start = 0
    end = max(tree_heights)

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cutting_sum = sum([height-mid if height-mid > 0 else 0 for height in tree_heights])
        if cutting_sum >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    tree_heights = list(map(int, input().rstrip().split()))
    print(solve(N, M, tree_heights))