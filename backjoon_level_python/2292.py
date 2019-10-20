def honey_comb(n):
    i = 1
    while n > 1:
        n -= 6 * i
        i += 1
    return i

n = int(input())
i = 1
while n > 1:
    n -= 6 * i
    i += 1
print(i)


def test_honey_comb():
    assert honey_comb(13) == 3
    assert honey_comb(1) == 1
    assert honey_comb(2) == 2
    assert honey_comb(7) == 2
    assert honey_comb(8) == 3


if __name__ == '__main__':
    print(honey_comb(int(input())))

