T = int(input())





for i in range(T):
    _OX = input()
    sum = 0
    val = 1
    for idx,s in enumerate(_OX):
        if s == 'O':
            sum = sum + val
            val = val + 1
        else:
            val = 1
    print(sum)
    
