A = int(input())
B = int(input())
C = int(input())

_mul = A*B*C

cnt_lt = [0]*10
while _mul:
    cnt_lt[_mul%10] = cnt_lt[_mul%10]+1
    _mul = _mul // 10

for i in range(10):
    print(cnt_lt[i])
    