
def sum_input(a, b):
    return a+b


def test_sum_input():
    assert sum_input(3, 5) == 8
    assert sum_input(0, 3) == 3


for i in range(1, int(input())+1,1):
    inp1, inp2 = map(int, list(input().split()))
    print("Case #" + str(i) + ": " + str(inp1)+ " + " + str(inp2) + " = " + str(sum_input(inp1, inp2)))
