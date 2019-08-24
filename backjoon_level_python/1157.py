t = input()

li_alpha = [0]*26

t = t.upper()
# print(ord(B-"A")
for i in t:
    li_alpha[ord(i)-ord('A')] = li_alpha[ord(i)-ord('A')] + 1
# print(li_alpha)
max_idx = 0
for idx,s in enumerate(li_alpha):
    if li_alpha[idx]>li_alpha[max_idx]:
        max_idx = idx

# max 하나더 있는지 검사
cnt = 0
for idx,s in enumerate(li_alpha):
    if li_alpha[idx] == li_alpha[max_idx]:
        cnt = cnt + 1

if cnt>=2:
    print("?")
else:
    print(chr(ord('A')+max_idx))  
    