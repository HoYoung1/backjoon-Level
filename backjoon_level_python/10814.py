if __name__ == '__main__':
    N = int(input())
    users = []
    for id in range(N):
        age, name = input().split()
        users.append((int(age), name, id))
    users.sort(key=lambda x: (x[0], x[2]))
    for user in users:
        print(*user[:2])
