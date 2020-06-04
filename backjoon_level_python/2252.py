from collections import deque


def topology_sort():
    result = []

    dq = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            dq.append(i)
    for i in range(1, N+1):
        if not dq:
            print('사이클 발생')
            return
        x = dq.popleft()
        result.append(x)
        for idx, stu in enumerate(matrix[x]):
            in_degree[matrix[x][idx]] -= 1
            if in_degree[matrix[x][idx]] == 0:
                dq.append(matrix[x][idx])
    return result
                



    


if __name__ == '__main__':
    N, M = map(int,input().split())
    matrix = [[] for _ in range(N+1)]
    in_degree = [0]*(N+1)
    for _ in range(M):
        student1, student2 = map(int, input().split())
        matrix[student1].append(student2)
        in_degree[student2] += 1
    print(' '.join(map(str, topology_sort())))
    




        