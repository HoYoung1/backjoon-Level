import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processing character
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        # print(s)

        # check palindrome
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False