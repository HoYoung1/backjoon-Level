def divide_q(pre_s, pre_e, in_s, in_e):
    if pre_s > pre_e or in_s > in_e:
        return

    root = pre_order[pre_s]
    inorder_root_index = position[root]
    left_node_num = inorder_root_index - in_s

    divide_q(pre_s + 1, pre_s + 1 + left_node_num, in_s, inorder_root_index - 1)
    divide_q(pre_s + 1 + left_node_num, pre_e, inorder_root_index + 1, in_e)
    print(root, end=" ")




if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        pre_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        position = {}
        for idx, node in enumerate(in_order):
            position[node] = idx

        divide_q(0, n - 1, 0, n - 1)
        print()