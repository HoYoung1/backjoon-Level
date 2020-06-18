import bisect


def solve(N, crains, M, box_weights):
    result = 0

    crains.sort(reverse=True)

    box_weights.sort(reverse=True)

    if crains[0] < box_weights[0]:
        return -1

    while box_weights:
        for crain in crains:
            for idx, weight in enumerate(box_weights):
                if crain >= weight:
                    del box_weights[idx]
                    break
        result += 1

    return result


if __name__ == '__main__':
    N = int(input())
    crains = list(map(int, input().split()))
    M = int(input())
    box_weights = list(map(int, input().split()))

    print(solve(N, crains, M, box_weights))
