def alarm(t):
    h, m = list(map(int,t.split()))
    total = h*60 + m
    total = total - 45
    if total < 0:
        total = total + 24*60
    return str(total//60) + " " + str(total%60)

print(alarm(input()))


def test_alarm():
    assert alarm("10 10") == "9 25"
    assert alarm("0 0") == "23 15"
    assert alarm("23 0") == "22 15"
    assert alarm("0 15") == "23 30"
    assert alarm("10 10") == "9 25"
