answer_flag = None

def solve():
    global answer_flag

    def dfs(num, target):
        global answer_flag
        if answer_flag:
            return
        if len(str(num)) > 100:
            return
        if num % target == 0:
            print(num)
            answer_flag = True
        dfs(num*10, n)
        dfs(num*10 + 1, n)  


    while True:
        answer_flag = False
        n = int(input())
        if n == 0:
            break
        dfs(1, n)

if __name__ == '__main__':
    solve()

