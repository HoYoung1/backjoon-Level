from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     s[i], s[-(i+1)] = s[-(i+1)], s[i]
        s.reverse()
        # return s


if __name__ == '__main__':
    s = Solution()
    assert s.reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
    assert s.reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]