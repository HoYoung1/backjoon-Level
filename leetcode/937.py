from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        alphas = []

        for log in logs:
            log_splited = log.split()
            if log_splited[1].isdigit():
                digits.append(log)
            else:
                alphas.append(log)
        # print(sorted(alphas) + digits)
        return sorted(alphas, key=lambda log: (log.split()[1:], log.split()[0])) + digits


if __name__ == '__main__':
    s = Solution()
    assert s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]