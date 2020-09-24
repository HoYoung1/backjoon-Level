dp = [[[[[False] * 4 for _ in range(4)] for _ in range(51)] for _ in range(51)] for _ in range(51)] # dp[51][51][51][4][4]


def go(a, b, c, before, bbefore):
    if a < 0 or b < 0 or c < 0:
        return False
    if a == 0 and b == 0 and c == 0:
        return True
    if dp[a][b][c][before][bbefore]:
        return False
    dp[a][b][c][before][bbefore] = True
    ans[n - sum([a,b,c])] = 'A'

    if go(a-1,b,c,0,before):
        return True
    if before != 1:
        # 그 전에께 B가 아니라면
        ans[n - sum([a,b,c])] = 'B'
        if go(a, b-1,c,1,before):
            return True
    if before != 2 and bbefore != 2:
        ans[n - sum([a,b,c])] = 'C'
        if go(a,b,c-1,2,before):
            return True
    return False


if __name__ == '__main__':
    input_text = input()
    aNum = {
        'A': 0,
        'B': 0,
        'C': 0
    }
    for t in input_text:
        aNum[t] += 1
    n = len(input_text)
    ans = [0] * 50

    if(go(aNum['A'], aNum['B'], aNum['C'], 0, 0)):
        print(''.join(ans[:n]))
    else:
        print(-1)



