def solve(meetings):
    result = 0

    meetings.sort(key=lambda m:(m[1],m[0]))

    current_time = -1
    for s, e in meetings:
        if current_time <= s:
            current_time = e
            result += 1
    return result


if __name__ == '__main__':
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    print(solve(meetings))