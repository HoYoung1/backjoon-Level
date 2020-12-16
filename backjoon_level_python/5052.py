import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_leaf = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]

            if curr.is_leaf is True:
                return False
        curr.is_leaf = True
        return True


def solve(phone_numbers):
    root = TrieNode()
    for number in phone_numbers:
        if root.insert(number) is False:
            return "NO"
    return "YES"


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        phone_numbers = [input().strip() for _ in range(n)]
        phone_numbers.sort(key=lambda p: len(p))

        print(solve(phone_numbers))


            
        
        
        
            

