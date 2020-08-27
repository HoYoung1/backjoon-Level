def solve(N, S, numbers):
    answer = 0
    A = []
    B = []

    def dfs(depth, last_depth, current_sum, target):
        if depth == last_depth:
            return
        target.append(current_sum + numbers[depth])
        dfs(depth + 1, last_depth, current_sum + numbers[depth], target)
        dfs(depth + 1, last_depth, current_sum, target)

    dfs(0, N//2, 0, A)
    dfs(N // 2, N, 0, B)
    A.append(0)
    B.append(0)
    A.sort()
    B.sort()
    # print(A)
    # print(B)
    A_pointer = 0
    B_pointer = len(B)-1
    while A_pointer < len(A) and B_pointer >= 0:
        if A[A_pointer] + B[B_pointer] < S:
            # 두 합은 커져야함
            A_pointer += 1
        elif A[A_pointer] + B[B_pointer] > S:
            # 두 합은 작아져야함
            B_pointer -= 1
        else:
            # 갯수 같은것들은 곱셈해줘야함
            A_same, B_same = 1, 1

            while A_pointer + 1 < len(A) and A[A_pointer + 1] == A[A_pointer]:
                A_same += 1
                A_pointer += 1
            while B_pointer - 1 >= 0 and B[B_pointer - 1] == B[B_pointer]:
                B_same += 1
                B_pointer -= 1
            answer += A_same * B_same

            A_pointer += 1
            B_pointer -= 1
    # 이 조건 왜 있는거지
    if S == 0:
        answer -= 1
    return answer


if __name__ == '__main__':
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solve(N, S, numbers))

    # assert solve(5, 0, [-7, -3, -2, 5, 8]) == 1
    # assert solve(3, 0, [0, 0, 0]) == 7
    # assert solve(40, 0, list(map(int, "100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000 -100000".split()))) == 137846528819