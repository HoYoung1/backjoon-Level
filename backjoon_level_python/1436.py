def solve(N):
    titles = set()
    titles.add(666)
    for i in range(10000):
        titles.add(int('666' + str(i)))
        titles.add(int(str(i) + '666'))
    sorted_titles = sorted(list(titles))
    print(sorted_titles)
    return sorted_titles[N-1]


def solve2(N):
    sorted_titles = []
    num = 1
    cnt = 0
    while True:
        if '666' in str(num):
            sorted_titles.append(num)
            cnt += 1
            if cnt == N:
                break
        num += 1
    print(sorted_titles)
    return num


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
    print(solve2(N))