if __name__ == '__main__':
    G = int(input())
    current, memory = 2, 1

    answer = []

    while True:
        current_square = current ** 2
        memory_square = memory ** 2
        if current-memory == 1 and G < current_square - memory_square:
            break

        if current_square - memory_square == G:
            answer.append(current)
            current += 1
            memory += 1
        elif current_square - memory_square > G:
            memory += 1
        else:
            current += 1

    if not answer:
        print(-1)
    else:
        for a in answer:
            print(a)


