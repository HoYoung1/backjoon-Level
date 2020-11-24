import sys
input = sys.stdin.readline

def solve(n, b, parts):
    # list to dict
    part_dict = {}
    for part in parts:
        type, name, price, quality = part
        if type in part_dict:
            part_dict[type].append((price, quality))
        else:
            part_dict[type] = [(price, quality)]
    # print('part_dict ', part_dict)

    def is_valid(budget, standard_quality):
        for type in part_dict:
            for price, quality in part_dict[type]:
                if int(quality) >= standard_quality:
                    budget -= int(price)
                    break
            else:
                return False
        if budget >= 0:
            return True
        return False

    # quality 가지고 이분탐색 조지자
    left = 0
    right = 1000000000
    while left < right:
        mid = (left + right) // 2
        if is_valid(b, mid):
            left = mid
        else:
            right = mid-1
    return right


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(T):
        n, b = list(map(int, input().rstrip().split()))  # 부품의 개수 n, 상근이의 예산 b
        parts = [input().rstrip().split() for _ in range(n)]
        print(solve(n, b, parts))
