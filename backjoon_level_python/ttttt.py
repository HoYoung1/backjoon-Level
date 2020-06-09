# # a = []
# # a.append((i,0) for i in range(1,46))
# #
# #
# # def solve(lottos):
# #     bonus = {}
# #     num_dic = {}
# #     for lotto in lottos:
# #         numbers = lotto.split()
# #         for num in numbers:
# #             if num[0] == '(':
# #                 if num in bonus:
# #                     bonus[num] += 1
# #                 else:
# #                     bonus[num] = 1
# #             else:
# #                 if num in num_dic:
# #                     num_dic[num] += 1
# #                 else:
# #                     num_dic[num] = 1
# #     temp_numbers = []
# #
# #     for num in num_dic:
# #         temp_numbers.append([int(num), num_dic[num]])
# #     temp_bonuses = []
# #     for num in bonus:
# #         temp_bonuses.append([int(num[1:-1]), bonus[num]])
# #     temp_numbers.sort(key=lambda x:(-x[1],x[0]))
# #     temp_bonuses.sort(key=lambda x:(-x[1],x[0]))
# #     print(temp_bonuses)
# #     print(temp_numbers)
# #
# #
# #     for li in temp_numbers[:5]:
# #         answer
# #
# #
# #
# # if __name__ == '__main__':
# #     solve(["52 18 7 9 (17) 6 1", "1 2 3 4 (5) 6 7"])
#
#
# # solve("APPLE",["LLZKE",'LCXEA', 'CVPPS', 'EAVSR', 'FXPFP']) == 3
#
#
# answer = 0
# def solve(word, cards):
#     visit = [False] * len(cards)
#
#     def dfs(depth, current, cards):
#         global answer
#         print(current)
#         if sorted(word) == sorted(current):
#             answer += 1
#
#         for i in range(len(cards)):
#             if not visit[i]:
#                 visit[i] = True
#                 dfs(depth+1, current+cards[depth][i],cards)
#                 visit[i] = False
#         cards = cards[1:] + cards[0]
#     dfs(0,'',cards)
#     return answer
# # print(solve("APPLE",["LLZKE",'LCXEA', 'CVPPS', 'EAVSR', 'FXPFP']))
# # answer = 0
# print(solve("BA",["123", "abc","456"]))
# # print(solve('BA',['ABB','ACB','DEF']))


def solve(word, cards):
    for i in len(cards)
        dfs(i)

    def dfs(start):


print(solve("BA", ["123", "abc", "456"]))