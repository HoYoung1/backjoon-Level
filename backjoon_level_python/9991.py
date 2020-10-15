import sys
input = sys.stdin.readline

if __name__ == '__main__':
    W, N = map(int, input().rstrip().split())
    dictionary = [input().rstrip() for i in range(W)]
    queries = [input().rstrip().split() for _ in range(N)]

    sorted_dictonary = sorted(dictionary)

    for query in queries:
        K_i, partial = query
        temp = []
        flag = False
        for word in sorted_dictonary:
            if word.startswith(partial):
                flag = True
                temp.append(word)
            elif flag is True:
                break
        try:
            w = temp[int(K_i)-1]
            print(dictionary.index(w)+1)
        except:
            print(-1)



