def test_1476():
    assert main(1, 16, 16) == 16
    assert main(1, 1, 1) == 1
    assert main(1, 2, 3) == 5266
    assert main(15, 28, 19) == 7980


def main(E, S, M):
    e = s = m = 1
    cnt = 1

    while True:
        if e == E and s == S and m == M:
            break

        e = e + 1
        if e == 16:
            e = 1
        s = s + 1
        if s == 29:
            s = 1
        m = m + 1
        if m == 20:
            m = 1
        cnt += 1
    return cnt
1

if __name__ == '__main__':
    E, S, M = map(int, input().split())
    print(main(E, S, M))