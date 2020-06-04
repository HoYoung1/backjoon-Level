def solve(n, k, numbers):
    raise NotImplementedError


if __name__ == '__main__':
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solve(n,k,numbers))

    assert solve(8, 3, [1,2,3,4,5,6,7,8]) == 3
    assert solve(8, 4, [1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert solve(8, 5, [1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert solve(1,1,[1]) == 1

    assert solve(1, 1, [2]) == 0
    assert solve(2, 1, [1,2]) == 1
    assert solve(2, 2, [1,2]) == 1
    assert solve(2, 1, [2,4]) == 0
    assert solve(2, 2, [2, 4]) == 0




