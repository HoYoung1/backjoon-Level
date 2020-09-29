import sys


def get_swaped_text(input_text, i, j):
    return input_text[:i] + input_text[j] + input_text[i+1:j] + input_text[i] + input_text[j+1:]


def get_min_palindrom(text):
    dp = [[sys.maxsize]*len(text) for _ in range(len(text))]
    # dp[i][j] = [text i ~ text j] 팰린드롬을 위한 최소 변경 횟수

    for i in range(len(text)):  # text[i][i] 는 팰린드롬 0
        dp[i][i] = 0

    for i in range(len(text)-1): # text[i][i+1] 는 팰린드롬 0 혹은 1
        dp[i][i+1] = 0 if text[i] == text[i+1] else 1

    for k in range(2, len(text)):
        for i in range(0, len(text)-k):
            j = i + k
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1, dp[i+1][j]+1, dp[i+1][j-1] if text[i] == text[j] else dp[i+1][j-1] + 1)
    return dp[0][len(text)-1]


def solve(input_text):
    answer = sys.maxsize

    for i in range(len(input_text)):
        for j in range(i+1, len(input_text)):
            text = get_swaped_text(input_text, i, j)
            answer = min(answer, get_min_palindrom(text) + 1)
    answer = min(answer, get_min_palindrom(input_text)) # 4번을 안했을때도 구해줘야함
    return answer


if __name__ == '__main__':
    input_text = input()
    print(solve(input_text))