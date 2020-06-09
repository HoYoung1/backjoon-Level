def solve(N, K):
    five_count = str(N).count('5')
    if five_count > K:
        return N + 1
    if len(str(N)) < K:
        return int("5"*K)
    if five_count == K:
        temp = 1
        for s in reversed(str(N)):
            if s == '5':
                temp *= 10
            else:
                break
        while True:
            N += temp
            if str(N).count('5') == K:
                return N
    if len(str(N)) > K:
        result = int(str(N)[:-K] + "5"*K)
        if result <= N:
            result = int(str(int(str(N)[:-K])+1) + "5" * K)
        return result


if __name__ == '__main__':
    N, K = map(int,input().split())
    print(solve(N, K))
    # assert solve(595,2) == 655
    # assert solve(595,1) == 596
    # assert solve(5,1) == 15
    # assert solve(998,4) == 5555
    # assert solve(41985,1) == 41995
    # assert solve(305555,1) == 305556
    # assert solve(305555, 4) == 315555
    # assert solve(305555, 5) == 355555
        # assert solve(59595, 3) == 59655
    #
    # assert solve(355559, 5) == 455555
5