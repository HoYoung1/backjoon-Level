# alpha = []

# for i in range(0,26):
#     alpha.append(chr((ord('A')+i)))

alpha = ""

for i in range(0,26):
    alpha+=chr(ord('A')+i)

def rt_val(c):
    if c in alpha[0:3]:
        return 2
    elif c in alpha[3:6]:
        return 3
    elif c in alpha[6:9]:
        return 4
    elif c in alpha[9:12]:
        return 5
    elif c in alpha[12:15]:
        return 6
    elif c in alpha[15:19]:
        return 7
    elif c in alpha[19:22]:
        return 8
    elif c in alpha[22:27]:
        return 9

def answer(txt):
    sum = 0
    for i in txt:
        t = rt_val(i)+1
        sum+=t
    return sum

print(answer(input()))

def test_answer():
    assert answer("UNUCIC") == 36


    
    