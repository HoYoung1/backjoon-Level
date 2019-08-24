max_idx = 0
max_val = 0
for i in range(1, 10, 1):
    inp_val = int(input())
    if inp_val > max_val:
        max_idx = i
        max_val = inp_val
print(max_val)
print(max_idx)
    