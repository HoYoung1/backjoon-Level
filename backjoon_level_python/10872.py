def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def test_factorial():
    assert factorial(10) == 3628800


print(factorial(int(input())))



