lt = []
for i in range(5):
    x = int(input())
    if x < 40:
        x = 40
    lt.append(x)
print(sum(lt)//len(lt))
