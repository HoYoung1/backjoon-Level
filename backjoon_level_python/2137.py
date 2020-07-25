import sys
from fractions import Fraction


def solve1():
    min_distance = sys.maxsize
    target = numerator / denominator  # numerator 분자 , denominator 분모
    # print('target', target)

    i = 1
    l = []
    while denominator * i <= 32767:
        l.append((numerator * i ,denominator * i))
        i += 1


    max_denominator = 32767

    for i in range(2, 32768):
        start = 1
        end = i
        mid = (start + end) // 2

        while start <= end:
            if (start + end) // 2 == i:
                # print('분자는 분모보다 작아야하므로 break')
                break

            mid = (start + end) // 2
            decimal = mid / i
            # print('decimal : {}'.format(decimal))

            if decimal > target:
                end = mid - 1
            elif decimal < target:
                start = mid + 1
            else:
                # print('current mid : {}'.format(mid))
                # print('loop end')
                break
        if target < mid/i:
            mid -= 1
        # print('찾은 mid 값 : {} = 현재 분모에서의 가장 target보다 작으면서 가장 가까운 값'.format(mid))
        distance = abs(target - mid/i)
        if distance < min_distance and (mid, i) not in l:
            min_distance = distance
            min_numerator = mid
            min_denominator = i

        if mid + 1 < i:
            mid += 1

        distance = abs(target - mid / i)
        if distance < min_distance and (mid, i) not in l:
            min_distance = distance
            min_numerator = mid
            min_denominator = i

    result = str(Fraction(min_numerator, min_denominator))
    a, b = result.split('/')

    # 원래는 위에꺼 답 하면 되는데 문제에 자기 자신과는 달라야한다는 조건이 있음.
    if a == numerator and b == denominator:
        # print('자신과 같네요..')
        result = Fraction(mid - 1, max_denominator)
        a, b = result.split('/')
    print(a, b, end=' ')
    # print('min distance', min_distance)
    # print('답 실수 : ', int(a) / int(b))

if __name__ == '__main__':
    numerator, denominator = map(int, input().split())

    target = numerator / denominator
    # print('target',target)

    solve1()








