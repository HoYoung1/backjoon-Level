# 70892KB 2156ms
# https://www.acmicpc.net/problem/1644

def get_prime_number(N):
    result = []
    visited = [True] * (N + 1)
    visited[0] = visited[1] = False
    for idx, flag in enumerate(visited):
        if flag is True:
            result.append(idx)
            i = 1
            while idx * i <= N:
                visited[idx * i] = False
                i += 1
    return result


def solve(N):
    primes = get_prime_number(N)

    start_index = 0
    end_index = 0
    current_sum = 0
    answer = 0

    while end_index < len(primes):
        if current_sum < N:
            current_sum += primes[end_index]
            end_index += 1
        while current_sum > N:
            current_sum -= primes[start_index]
            start_index += 1
        if current_sum == N:
            answer += 1
            current_sum -= primes[start_index]
            start_index += 1
    return answer


if __name__ == '__main__':
    N = int(input())
    print(solve(N))