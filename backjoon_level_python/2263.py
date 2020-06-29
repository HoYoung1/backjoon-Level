    # https://tttuer.tistory.com/174 참고
    import sys
    sys.setrecursionlimit(10**9)

    def solve(inorder_s, inorder_e, post_s, post_e):
        if inorder_s > inorder_e or post_s > post_e:
            return

        root = post_order[post_e]
        print(root, end=' ')

        inorder_root_idx = position[root]
        # print('inorder_root_idx : ', inorder_root_idx)

        left = inorder_root_idx - inorder_s
        solve(inorder_s, inorder_root_idx-1, post_s, post_s + left -1)
        solve(inorder_root_idx+1,inorder_e, post_s + left, post_e - 1)


    if __name__ == '__main__':
        n = int(input())
        in_order = list(map(int, input().split()))
        post_order = list(map(int, input().split()))

        position = {}
        for i in range(n):
            num = in_order[i]
            position[num] = i

        solve(0, n-1, 0, n-1)

