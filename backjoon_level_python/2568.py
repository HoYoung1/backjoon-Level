import bisect
import sys


def solve(N, electric_wires):
    answer = []
    lis_answer = 0
    trace = [-1]*(N)
    visited = [False]*N
    electric_wires.sort(key=lambda wire:wire[0])

    new_electric_wires = [electric_wire[1] for electric_wire in electric_wires]
    list_table = [-sys.maxsize]

    # print(new_electric_wires)
    for i, wire in enumerate(new_electric_wires):
        if list_table[-1] < wire:
            list_table.append(wire)
            trace[i] = len(list_table)-1
            lis_answer += 1
        else:
            # 이분탐색
            idx = bisect.bisect_left(list_table[1:], wire)
            list_table[idx+1] = wire
            trace[i] = idx+1

    # print(trace)
    tracing = lis_answer
    print(N-lis_answer)
    for i in range(len(trace)-1,-1,-1):
        if trace[i] == tracing:
            visited[i] = True
            tracing -= 1
    for i in range(len(visited)):
        if visited[i] == False:
            print(electric_wires[i][0])


if __name__ == '__main__':
    N = int(input())
    electric_wires = [list(map(int,input().split())) for _ in range(N)]
    solve(N, electric_wires)
