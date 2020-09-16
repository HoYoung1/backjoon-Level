def solve(N, beads):
    beads = [0] + beads + [0] * (5-len(beads))
    # memo[11][11][11][11][11][6][6]
    memo = [[[[[[[-1] * 6 for _ in range(6)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

    def dfs(beads, before, bbefore):
        # 이미 메모 되어있으면
        if before != -1 and bbefore != -1: # 맨처음회
            if memo[beads[1]][beads[2]][beads[3]][beads[4]][beads[5]][before][bbefore] != -1:
                return memo[beads[1]][beads[2]][beads[3]][beads[4]][beads[5]][before][bbefore]

        # 구슬 다썼으면
        if beads[1] == 0 and beads[2] == 0 and beads[3] == 0 and beads[4] == 0 and beads[5] == 0:
            return 1

        temp = 0
        for idx in range(1,6):
            if beads[idx] >= 1 and before != idx and bbefore != idx:
                beads[idx] -= 1
                temp += dfs(beads, idx, before)
                beads[idx] += 1

        memo[beads[1]][beads[2]][beads[3]][beads[4]][beads[5]][before][bbefore] = temp
        return memo[beads[1]][beads[2]][beads[3]][beads[4]][beads[5]][before][bbefore]

    answer = dfs(beads, -1, -1)
    return answer




if __name__ == '__main__':
    N = int(input())
    beads = [int(input()) for _ in range(N)]

    print(solve(N, beads))