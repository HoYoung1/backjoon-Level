from fractions import Fraction

def p(a,b):
    s = str(Fraction(a,b))
    if '/' not in s:
        s += '/1'
    print(s)

n = input()
if '(' not in n:
    if '.' in n:
        a,b  = n.split('.')
        k = 10 ** len(b)
        l = a + b
        p(int(l),k)
    else:
        print(n,'/',1,sep='')
else:
    s = n.split('(')
    c = s[1][:-1]
    a, b = s[0].split('.')
    q = int(a + b + c)
    w = int(a + b)

    k = 10 ** (len(b) + len(c)) - 10 ** (len(b))
    l = q - w
    p(l,k)