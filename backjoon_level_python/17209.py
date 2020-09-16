import sys
sys.setrecursionlimit(10**8)

def dfs(current, old):
    if visited[current]:
        return
    visited[current] = True
    for i in edges[current]:
        if visited[i]:
            continue
        people[not old] += 1
        dfs(i, not old)


if __name__ == '__main__':
    N = int(input())
    visited = [False] * (N+1)
    edges = {i: set() for i in range(1, N+1)}
    people = [0] * 2
    res = 0

    for i in range(1, N+1):
        reports = input()
        for j in range(1, N+1):
            if reports[j-1] == '1':
                edges[i].add(j)
                edges[j].add(i)

    for i in range(1, N+1):
        if visited[i]:
            continue
        people[0] = 0
        people[1] = 0
        dfs(i, True)
        res += max(people[0], people[1] + 1)
    print(res)




