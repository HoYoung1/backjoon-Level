import sys
sys.setrecursionlimit(10**8)


def solve(number: str):
    success = False

    def dfs(num: str):
        nonlocal success

        if success:
            return

        for i in '1234567890':
            if str(int(i + num) ** 3)[-len(num+i):] == number[-len(num+i):]:
                if len(i + num) == len(number):
                    success = True
                    print(int(i + num))
                    break
                dfs(i+num)

    dfs('')


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve(input())