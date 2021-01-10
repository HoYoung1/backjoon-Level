from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = dict()
        # for str in strs:
        #     c = dict(Counter(str))
        #     if c in dic:
        #         dic[c].append(str)
        #     else:
        #         dic[c] = [str]
        # print(dic)

        dic = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dic:
                dic[sorted_str].append(str)
            else:
                dic[sorted_str] = [str]
        print(list(dic.values()))
        return dic.values()


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])