class TrieNode:
    def __init__(self):
        self.nodes = {}

    def insert(self, words):
        curr = self
        for word in words:
            if word not in curr.nodes:
                curr.nodes[word] = TrieNode()
            curr = curr.nodes[word]

    def render(self, depth, node):
        for word in sorted(node.nodes):
            print("--" * depth + word)
            self.render(depth + 1, node.nodes[word])


def solve(trie_root):
    trie_root.render(0, trie_root)


if __name__ == '__main__':
    N = int(input())
    root = TrieNode()
    for _ in range(N):
        words = input().split()
        words = words[1:]
        root.insert(words)
    solve(root)

