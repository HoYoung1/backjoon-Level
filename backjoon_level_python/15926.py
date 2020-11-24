class Stack:
    def __init__(self):
        self.contents = []

    def is_empty(self):
        return len(self.contents) == 0

    def push(self, item):
        self.contents.append(item)

    def top(self):
        return self.contents[-1]

    def pop(self):
        return self.contents.pop()


def solve(n, bracket):
    stk = Stack()
    answer = 0

    stk.push(-1)
    for idx, s in enumerate(bracket):
        if s == '(':
            stk.push(idx)
        else:
            stk.pop()
            if stk.is_empty():
                stk.push(idx)
            else:
                answer = max(answer, idx - stk.top())
    return answer


if __name__ == '__main__':
    n = int(input())
    bracket = input()

    print(solve(n, bracket))
    #
    # assert solve(5, '(())(') == 4
    # assert solve(14, '(()))()((()))(') == 8
    #
    # assert solve(0, ')()(') == 2
    # assert solve(0, '))(') == 0
    # assert solve(0, '((())))(((()))') == 6
    # assert solve(0, '(())') == 4
    # assert solve(0, '))))))') == 0
    # assert solve(0, '()((())') == 4