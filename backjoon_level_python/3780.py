import sys
sys.setrecursionlimit(10**8)

# 2
# 4
# E 3
# I 1 3
# E 3
# I 3 4
# E 3
# O

def find(v, distance):
    if arr[v][0] == v:
        return v, arr[v][1]
    # distance += arr[v][1]  # 확인해봐야함
    u, dis = find(arr[v][0], arr[v][1])
    arr[v][1] += dis
    return u, arr[v][1]


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input()) # 4<=N<=20000
        arr = [[i, 0] for i in range(N+1)]
        while True:
            order = input().split()
            if order[0] == 'O':
                arr = [[i, 0] for i in range(N+1)]
                break
            elif order[0] == 'E':
                u = int(order[1])
                parent, distance = find(u, 0)
                arr[u][0] = parent
                # print('u : {} , parent : {}, distance : {}'.format(u, parent, distance))
                print(distance)
            elif order[0] == 'I':
                u, v = int(order[1]), int(order[2]) # u => v
                distance = abs(u-v) % 1000
                # p1, d1 = find(v, 0)
                # p1 = find(v, distance)
                arr[u][0] = v
                arr[u][1] = distance
                # p2 = get_parent(v)
                # print('u, v 갱신', u ,v)
            # print('현재 arr',arr)


