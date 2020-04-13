queue = []
count = 0


def isSafe(row, column):
    for x, y in queue:
        if column == y or abs(row-x) == abs(column-y):
            return False
    return True


def solve(row):
    global count
    if row >= len(board):
        count += 1
        return
    for i in range(len(board)):
        if isSafe(row, i):
            queue.append((row, i))
            solve(row + 1)
            queue.remove((row, i))
    return False


n = int(input())
board = [[0 for i in range(n)] for j in range(n)]
solve(0)
print(count)

204008	31864