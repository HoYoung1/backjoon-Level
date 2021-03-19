if __name__ == '__main__':
    x_set = set()
    y_set = set()
    for i in range(3):
        x, y = input().split()
        if x in x_set:
            x_set.remove(x)
        else:
            x_set.add(x)
        if y in y_set:
            y_set.remove(y)
        else:
            y_set.add(y)
    print(''.join(x_set), ''.join(y_set))



