# def check_group_word(str_t):
#     li_alpha = [0]*26
#     for idx,s in enumerate(str_t):
#         if len(str_t)>idx+1 and str_t[idx]!=str_t[idx+1]:
#             li_alpha[ord(str_t[idx])-ord('a')] = li_alpha[ord(str_t[idx])-ord('a')] +1
#         elif idx+1 == len(str_t): # 마지막이라면
#             li_alpha[ord(str_t[idx])-ord('a')] = li_alpha[ord(str_t[idx])-ord('a')]+1
#         if li_alpha[ord(str_t[idx])-ord('a')] >1:
#             return False
#     return True

# t = int(input())
# cnt = 0
# for i in range(t):
#     if check_group_word(input()) == True:
#         cnt = cnt + 1
# print(cnt)

# result = 0
# for i in range(int(input())):
#     word = input()
#     print(list(word))
#     print(sorted(word))
#     if list(word) == sorted(word):
#         result += 1
# print(result)

# result = 0

# for i in range(int(input())):
#         ip = input()
#         print(list(ip))
#         print(sorted(ip))
#         if list(ip) == sorted(ip):
#                 result+=1
                
# print(result)

for i in range(int(input())):
        _string = input()
        li = []
        for idx, s in enumerate(_string):
                if idx+1 == len(string): # 마지막은 다음껄 검사하면안됨
                        break
                if _string[idx] not in li = []:
                        li.append(_string[idx])
                        continue
                
                if _string[idx] == _string[idx+1]:
                        continue
                
