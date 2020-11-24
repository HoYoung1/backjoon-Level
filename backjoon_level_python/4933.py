from collections import deque


class Node:
    def __init__(self):
        self.parent = 0
        self.left = 0
        self.right = 0


def makeTree(node):
    input_text = input().split()
    str = []  # vector<char> str;
    for text in input_text:
        if text == 'end':
            break
        if text == 'nil':
            str.append(0)
        else:
            str.append(text)

    stk = deque()
    for i in range(len(str)):
        curr = str[i if isinstance(i, int) else ord(i)]
        if curr == 0:
            stk.append(0)
        else:
            if len(stk) >= 2:
                right = stk.pop()
                left = stk.pop()
                print('right', right)
                print('left', left)

                node[right if isinstance(right, int) else ord(right)].parent = curr
                node[left if isinstance(left, int) else ord(left)].parent = curr

                node[curr if isinstance(curr, int) else ord(curr)].right = right
                node[curr if isinstance(curr, int) else ord(curr)].left = left
            stk.append(curr)

    if len(stk) == 0:
        return 0
    else:
        return stk[0]


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        node1 = [Node() for _ in range(100)]
        node2 = [Node() for _ in range(100)]
        root1 = makeTree(node1)
        root2 = makeTree(node2)
        # print('node1', node1)
        # print('node2', node2)
        print('root1', root1)
        print('root2', root2)

        chk = root1 == root2
        for i in range(ord('A'), ord('Z')):
            chk &= node1[i].parent == node2[i].parent
        print("true" if chk is True else "false")