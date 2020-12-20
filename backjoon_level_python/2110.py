def check(distance):
    count = 1
    current = coordinates[0]
    for x in coordinates[1:]:
        if current + distance <= x:
            count += 1
            current = x
    if count >= C:
        return True
    return False


def solve(N, C, coordinates):
    start = 0
    end = max(coordinates)

    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


if __name__ == '__main__':
    N, C = map(int, input().split())
    coordinates = [int(input()) for _ in range(N)]
    coordinates.sort()

    print(solve(N, C, coordinates))