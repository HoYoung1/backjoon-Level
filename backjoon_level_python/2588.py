a = int(input())
b = input()

def multi(a,b):
    s_num = 0
    for idx,i in reversed(list(enumerate(b))):
        pos = (10**(len(b)-1-idx))
        n = a*int(i)
        print(n)
        s_num += n*pos
    return s_num

print(multi(a,b))

def test_multi():
    assert multi(472,str(385)) == 181720
    
