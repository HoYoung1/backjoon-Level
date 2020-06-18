def solve(N, K, sensors):
    sensors.sort(reverse=True)
    distances = sorted([sensors[i]-sensors[i+1] for i in range(len(sensors)-1)], reverse=True)
    return sum(distances[K-1:])


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    sensors = list(map(int, input().split()))
    print(solve(N,K,sensors))