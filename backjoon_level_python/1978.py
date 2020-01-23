list_prime = []

def is_prime(num):
    if list_prime[num]:
        return True
    return False


def set_prime_list(N):
    global list_prime
    list_prime = [True] * (N+1)
    list_prime[0] = list_prime[1] = False # 0, 1은 소수가 아님
    for i in range(2, len(list_prime)):
        if list_prime[i] is True:
            # this is prime number
            temp = i
            j = 2
            while temp*j <= 1000:
                list_prime[temp * j] = False
                j += 1
    #
    # for idx, v in enumerate(list_prime):
    #     if v:
    #         print(idx)


if __name__ == '__main__':
    _ = input()
    set_prime_list(1000) # 1000 이하의 자연수

    total_prime_num = 0
    for i in list(map(int, input().split())):
        if is_prime(i):
            total_prime_num += 1
    print(total_prime_num)