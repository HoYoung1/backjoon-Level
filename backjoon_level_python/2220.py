if __name__ == '__main__':
    n = int(input())

    hq = [1] * (n+1)  # start from idx 1
    for i in range(2, n+1):
        hq[i-1] = i  # 마지막 요소에 i를 추가. (1이 지워짐)

        # 추가 후 올리는 작업
        j = i-1
        while j//2 >= 1:
            hq[j], hq[j//2] = hq[j//2], hq[j]
            j = j//2
    print(' '.join(map(str, hq[1:])))