N = int(input())

def hansu(N):
    if N<100:
        return N
    else:
        cnt = 0
        for i in range(100,N+1):
            first = i%10
            i = i//10
            second = i%10
            i = i//10
            third = i
            if third - second == second - first:
                cnt = cnt + 1
        return 99+cnt


# print(N)
print(hansu(N)) 
