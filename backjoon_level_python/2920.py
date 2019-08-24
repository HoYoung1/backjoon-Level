ascending = [1,2,3,4,5,6,7,8]
lt = list(map(int,input().split()))
a=input()[::2]
print("ㅅㅂㅅㅂㅅㅂㅅㅂㅅㅂ"*5,a)
if lt==ascending:
    print("ascending")
elif list(reversed(ascending))==lt:
    print("descending")
else:
    print("mixed")