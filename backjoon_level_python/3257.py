def solve():
    dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

    dp[0][0] = 999
    for i in range(0, len(word1)+1):
        for j in range(0, len(word2)+1):
            if i != 0 and dp[i-1][j] != 0 and word1[i-1] == mixed_word[i+j-1]:
                dp[i][j] = 1
            if j != 0 and dp[i][j-1] != 0 and word2[j-1] == mixed_word[i+j-1]:
                dp[i][j] = 2
    for row in dp:
        print(row)
    print()
    
    a = len(word1)
    b = len(word2)
    answer = ''
    for i in range(len(word1)+len(word2)):
        answer = str(dp[a][b]) + answer
        if dp[a][b] == 1:
            a -= 1
        else:
            b -= 1

    return answer


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    mixed_word = input()

    print(solve())