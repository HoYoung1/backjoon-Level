def solve(numbers):
    tree_levels = {i: [] for i in range(1, 1001)}
    level = 1
    before = numbers[0] - 1

    current = 0
    desired = 1
    # make tree level
    for number in numbers:
        if before+1 != number:
            current += 1
            if current == desired:
                current = 0
                desired = len(tree_levels[level])
                level += 1
        tree_levels[level].append(number)
        before = number

    print(tree_levels)
    for i in range(1, 1001):
        if k <= tree_levels[i][-1]:
            idx = tree_levels[i].index(k)

            # 왼쪽 오른쪽 보며 그 갯수 보기
            count = 1

            before = tree_levels[i][idx]
            left = idx - 1
            while 0<=left and before == tree_levels[i][left] + 1:
                before = tree_levels[i][left]
                count += 1
                left -= 1

            before = tree_levels[i][idx]
            right = idx +1
            while right < len(tree_levels[i]) and before + 1 == tree_levels[i][right]:
                before = tree_levels[i][right]
                count += 1
                right += 1
            # print('count', count)
            return len(tree_levels[i]) - count





if __name__ == '__main__':
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        numbers = list(map(int, input().split()))
        print(solve(numbers))
