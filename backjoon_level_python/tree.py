class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    root = Node(5)
    root.left = Node(1)
    root.right = Node(2)

    root.left.left = Node(3)

    return root


def preorder_traverse(node):
    if node is None:
        return
    print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


if __name__ == '__main__':
    root = init_tree()

    preorder_traverse(root)

