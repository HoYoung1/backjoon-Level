# TODO : 코드 하나씩 따라가보며 다시 해볼 필요있음. 아직 dp 미숙 ㅠ
# 카탈란 수 라는 것도 있음. 이것도 나중에 보면 좋을듯

def solve(N):
    def find(w, h):
        if w == 0 and h == 0:
            return 1
        elif w < 0 or h < 0:
            return 0
        elif dp[w][h] != -1:
            return dp[w][h]
        else:
            dp[w][h] = find(w-1, h+1) + find(w, h-1)
            return dp[w][h]
    return find(N, 0)


if __name__ == '__main__':
    dp = [[-1] * 31 for _ in range(31)]
    while True:
        N = int(input())   # 약의 개수 N ≤ 30
        
        if N == 0:
            break
        print(solve(N))
        