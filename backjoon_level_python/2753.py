# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or year % 400 ==0:
        return 1
    return 0

print(is_leap_year(int(input())))

def test_leap_year():
    assert is_leap_year(2000) == 1
    assert is_leap_year(1999) == 0
    assert is_leap_year(2012) == 1
    assert is_leap_year(1900) == 0

