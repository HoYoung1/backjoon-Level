if __name__ == '__main__':
    N = int(input())
    coordiates = []
    for i in range(N):
        x, y = map(int, input().split())
        coordiates.append((x, y))
    coordiates.sort(key=lambda k: (k[1], k[0]))
    for i in range(N):
        print(coordiates[i][0], coordiates[i][1])

