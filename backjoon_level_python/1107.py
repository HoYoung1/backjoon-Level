def min_click_btn(N, available_btns):
    min_num = abs(N - 100)
    for num in range(1000000):
        check_flag = True
        for i in str(num):
            if i not in available_btns:
                # Don't check
                check_flag = False
        if check_flag:
            min_num = min(abs(N-num)+len(str(num)), min_num)

    return min_num


if __name__ == '__main__':
    btns = [str(i) for i in range(10)]
    broken_btns = []

    N = int(input()) # 채널 N (0 ≤ N ≤ 500,000)
    M = int(input()) # 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다
    if M != 0:
        broken_btns = list(input().split()) # 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

    available_btns = list(set(btns) - set(broken_btns))
    # print(available_btns)

    print(min_click_btn(N, available_btns))
