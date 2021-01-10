from collections import Counter
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]',' ', paragraph).lower().split()
         if word not in banned]
        words = Counter(words)
        return words.most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()
    assert s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]) == "ball"