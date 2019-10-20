from swea_1953 import is_connected

N = 5
grid = [list(map(int, input().split())) for _ in range(N)]
print(is_connected((0, 0), (1, 0), grid))