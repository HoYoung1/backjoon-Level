"""
1 1
2 3
3 4
9 8
5 2
"""

while True:
    try:
        print(sum(map(int, input().split())))
    except Exception:
        exit()
