# 잘못접근
def solve(n, k, devices):
    answer = 0
    connected_devices = []
    waiting_devices = []
    for device in devices:
        if len(connected_devices) < n and device not in connected_devices:
            connected_devices.append(device)
            continue
        if not waiting_devices and device in connected_devices:
            continue
        if device not in connected_devices and device not in waiting_devices:
            waiting_devices.append(device)
            answer += 1
        elif device in waiting_devices:
            pass
        else:
            waiting_devices.append(device)
        if len(waiting_devices) == n:
            connected_devices = waiting_devices[:]
            waiting_devices = []
    return answer


def solve2(n, k, devices):
    answer = 0
    connected_devices = []
    waiting_devices = []
    for idx, device in enumerate(devices):
        if len(connected_devices) < n and device not in connected_devices:
            connected_devices.append(device)
        elif device in connected_devices:
            continue
        else:
            for connected_device in connected_devices:
                if connected_device not in devices[idx:]:
                    connected_devices.remove(connected_device) # 이 꽂혀있는 디바이스는 앞으로 안쓰므로 뺌^^
                    connected_devices.append(device)
                    answer += 1
                    break
            else:
                # 전부다 나중에 사용된다는거임. 그럼 가장 늦게 사용되는 디바이스를 빼라
                last_device_idx = -1
                for connected_device in connected_devices:
                    connected_device_idx = devices[idx:].index(connected_device)
                    if connected_device_idx > last_device_idx:
                        last_device_idx = connected_device_idx
                connected_devices.remove(devices[idx:][last_device_idx])
                connected_devices.append(device)
                answer += 1

    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    devices = list(map(int, input().split()))
    print(solve2(N, K, devices))

    assert solve2(2, 7, [2, 3, 2, 3, 1, 2, 7]) == 2
    assert solve2(3, 7, [2, 3, 2, 3, 1, 2, 7]) == 1
    assert solve2(4, 11, [1, 2, 3, 4, 1, 4, 5, 6, 10, 2]) == 3
    assert solve2(3, 11, [1, 2, 3, 4, 1, 4, 5, 6, 10, 2]) == 4
    assert solve2(3, 11, [11, 8, 11, 7, 2, 8, 2, 7, 5, 10, 2]) == 3
    assert solve2(2, 5, [5, 2, 2, 3, 5]) == 1
    assert solve2(2, 4, [5, 3, 1, 5]) == 1
    assert solve2(3, 6, [1, 1, 1, 1, 2, 3]) == 0
    assert solve2(3, 8, [1, 2, 3, 4, 1, 1, 1, 2]) == 1
    assert solve2(2, 15, list(map(int, '3 2 1 2 1 2 1 2 1 3 3 3 3 3 3'.split()))) == 2
    assert solve2(2, 11, list(map(int, '1 2 3 4 5 1 1 1 2 2 2'.split()))) == 4

