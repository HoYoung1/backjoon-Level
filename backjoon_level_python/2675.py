T = int(input())

for i in range(T):
    temp = list(input().split())
    temp[0] = int(temp[0])
    x=''
    for j in temp[1]:
        x = x+ j*temp[0]
    print(x)