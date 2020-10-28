class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []

    def add_child(self, current):
        print('current', current)
        self.children.append(Node(current))

    def get_parent(self):
        return self.parent


def solve(tree1, tree2):
    root = Node(None)
    idx = 0
    current = root
    for s in tree1:
        print('s', s)
        if s == '0':
            current.add_child(current)
        else:
            current = current.parent
    print(root)





    if get_tree_levels(tree1) == get_tree_levels(tree2):
        return '1'
    return '0'


if __name__ == '__main__':
    T = int(input())
    tree1, tree2 = input(), input()
    solve(tree1, tree2)

    