st = input()

lt = [-1] * 26

_a = ord('a')

for idx, s in enumerate(st):
    if lt[ord(st[idx]) - _a] != -1:
        continue
    else:
        lt[ord(st[idx]) - _a] = idx

for i in lt:
    print(i,end=" ")
        