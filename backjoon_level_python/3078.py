import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    friends = [len(input().rstrip()) for _ in range(N)]

    answer = 0
    dict_in_K = {i: 0 for i in range(21)}
    for i in range(len(friends)):
        answer += dict_in_K[friends[i]]
        dict_in_K[friends[i]] += 1
        if i >= K:
            dict_in_K[friends[i-K]] -= 1
    print(answer)

