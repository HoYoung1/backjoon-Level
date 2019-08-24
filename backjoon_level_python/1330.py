def comp(s):
    l = list(map(int,s.split(" ")))
    if l[0]>l[1]:
        return ">"
    elif l[0]<l[1]:
        return "<"
    else:
        return "=="
print(comp(input()))

def test_comp():
    assert comp("19 20") == "<"

def test_comp():
    assert comp("-21 20") == "<"
def test_comp():
    assert comp("-1 0") == "<"