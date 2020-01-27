def sieve_of_eratosthenes(maximum):
    primes = []
    primes_bool = [True] * (maximum + 1)
    primes_bool[0] = primes_bool[1] = False  # 0과 1은 검사할 필요 없음.
    for i in range(len(primes_bool)):
        if primes_bool[i] is True:
            primes.append(i)
            cnt = 2
            while True:
                # 그 소수의 모든 배수는 소수가 될 수 없음.
                if i * cnt > maximum_n:
                    break
                primes_bool[i*cnt] = False
                cnt += 1
    return primes, primes_bool


# 메모리 39016KB 시간 4584ms
def solution1(tc, primes, primes_bool):
    correct_flag = False
    for prime in primes:
        if primes_bool[tc - prime] is True:
            # 두 소수의 합으로 표현되면
            correct_flag = True
            print('{} = {} + {}'.format(tc, prime, tc - prime))
            break
    if correct_flag is False:
        print("Goldbach's conjecture is wrong.")


# 메모리 37096KB 시간 4620ms
def solution2(tc, primes_bool):
    correct_flag = False
    for idx, prime_bool in enumerate(primes_bool):
        if prime_bool is True:
            # 소수이면
            if primes_bool[tc - idx] is True:
                correct_flag = True
                print('{} = {} + {}'.format(tc, idx, tc - idx))
                break
    if correct_flag is False:
        print("Goldbach's conjecture is wrong.")


if __name__ == '__main__':
    maximum_n = 1000000 # 6 ≤ n ≤ 1000000
    primes, primes_bool = sieve_of_eratosthenes(maximum_n)

    # 두 '홀수' 소수의 합만 신경써야하므로 2는 지운다
    del primes[0]
    primes_bool[2] = False

    while True:
        tc = int(input())
        if tc == 0:
            break
        else:
            #solution1(tc, primes, primes_bool)
            solution2(tc, primes_bool)







