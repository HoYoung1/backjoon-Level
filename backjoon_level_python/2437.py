def solve(N, nums):
    nums.sort()
    S = 1 # sum
    for num in nums:
        if S < num:
            break
        else:
            S += num
    return S


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(solve(N, nums))