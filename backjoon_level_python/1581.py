if __name__ == '__main__':
    FF, FS, SF, SS = map(int, input().split())
    if FF == 0 and FS == 0:
        if SF == 0:
            print(SS)
        else:
            print(SS+1)
    elif FS == 0:
        print(FF)
    else:
        if FS <= SF:
            print(FF+FS+FS+SS)
        else:
            print(FF+SF+SF+SS+1)