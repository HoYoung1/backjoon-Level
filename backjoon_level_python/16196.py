from datetime import datetime


class IdValidator:
    def __init__(self):
        pass

    def _is_valid_location_code(self, identification, codes):
        return identification[:6] in codes

    def _is_valid_date(self, identification):
        ts_in_YYYYMMDD = identification[6:14] # 1900년 1월 1일부터 2011년 12월 31

        if not ('19000101' <= ts_in_YYYYMMDD <= '20111231'):
            return False

        try:
            datetime.strptime(ts_in_YYYYMMDD, '%Y%m%d')
            return True
        except Exception as e:
            # print(e)
            return False


    def _is_valid_ordered_code(self, identification):
        order_code = identification[14:17]
        if order_code == '000':
            return False
        return True

    def is_man_or_woman(self, identification):
        order_code = identification[14:17]
        if not self._is_valid_ordered_code(identification):
            return 'I'

        if int(order_code) % 2 == 0:
            return 'F'
        else:
            return 'M'

    def _is_valid_checksum(self, identification):
        checksum = identification[17]
        if checksum == 'X':
            checksum = 10
        else:
            checksum = int(checksum)

        temp_sum = 0
        for idx, c in enumerate(identification[:17]):
            temp_sum += int(c) * 2**(17-idx)

        # TODO : 이거... 더 좋은 식 없나?
        value = temp_sum % 11
        if value == 0:
            x = 1
        elif value == 1:
            x = 0
        else:
            x = 12 - value

        # print('x : {} , checksum : {}'.format(x, checksum))

        return x == checksum

    def is_valid_id(self, identification, codes):
        if not self._is_valid_location_code(identification, codes):
            return False
        elif not self._is_valid_date(identification):
            return False
        elif not self._is_valid_ordered_code(identification):
            return False
        elif not self._is_valid_checksum(identification):
            return False
        return True




def solve(identification, N, codes):
    answer = 0

    validator = IdValidator()
    if validator.is_valid_id(identification, codes):
        answer = validator.is_man_or_woman(identification)
    else:
        answer = 'I'
    return answer


if __name__ == '__main__':
    identification = input()
    N = int(input())
    codes = [input() for _ in range(N)]

    print(solve(identification, N, codes))

    # validator = IdValidator()
    # print(validator._is_valid_date('62012320020228058X'))
    # assert solve('441323200312060636', 1, ['441323']) == 'M'
    # assert solve('62012319240507058X', 1, ['620123']) == 'F'
    #
    # assert solve('321669197204300886', 2, ['610111','659004']) == 'I'
    # assert solve('230231198306900162', 1, ['230231']) == 'I'
    # assert solve('341400198407260005', 1, ['341400']) == 'I'
    #
    # assert solve('520381193206090891', 2, ['532922','520381']) == 'I'
    #
    #
    # assert solve('441323200312060636', 1, ['441323']) == 'M'
    #
    #
    #
    # assert solve('441323200312060636', 1, ['541323']) == 'I'
