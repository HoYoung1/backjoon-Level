# from unittest import TestCase
import math
#
# class TestAcmHotel(TestCase):
#     def test_acm_hotel(self):
#         self.assertEqual(acm_hotel(6, 12, 10), '402')
#         self.assertEqual(acm_hotel(30, 50, 72), '1203')
#         self.assertEqual(acm_hotel(1, 1, 1), '101')
#         self.assertEqual(acm_hotel(99, 99, 99), '9901')
#         self.assertEqual(acm_hotel(2, 9, 2), '201')


def acm_hotel(H, W, N):
    a = N % H
    if a == 0:
        a = H
    b = math.ceil(N/H)
    if b < 10:
        b = '0'+str(b)
    return str(a)+str(b)


if __name__ == '__main__':
    for _ in range(int(input())):
        H, W, N = map(int, input().split())
        print(acm_hotel(H, W, N))