from collections import deque


def solve1(N, relationships):
    # relationships.append([-1]) # 0번 인덱스 처리하기 위함
    building_times = [-1]
    for i in range(1, N + 1):
        input_data = input().split()

        building_time = int(input_data[0])
        building_times.append(building_time)

        dependencies = input_data[1:-1]
        for dependency in dependencies:
            relationships[int(dependency)].append(i)
    print(relationships)
    print(building_times)


def solve2(N, relationships):
    result = []
    building_times = [0] * (N+1)
    indegree_infos = [[] for _ in range(N+1)]
    max_times = [[] for _ in range(N+1)]

    for i in range(1, N + 1):
        input_data = input().split()

        parent_building_time = int(input_data[0])
        building_times[i] = parent_building_time

        dependencies = list(map(int, input_data[1:-1]))
        indegree_infos[i] = dependencies

        # convert
        for dependency in dependencies:
            relationships[int(dependency)].append(i)

    # print(relationships)
    indegree = []
    for v_list in indegree_infos:
        indegree.append(len(v_list))

    dq = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append((i,building_times[i]))

    for i in range(1, N+1):
        if not dq:
            # 큐가 비면 사이클이 생겼따는것임
            print('사이클 발생')
        vertex_idx, parent_building_time = dq.popleft()
        result.append(vertex_idx)
        building_times[vertex_idx] = parent_building_time
        for k in relationships[vertex_idx]:
            indegree[k] -= 1
            max_times[k].append(parent_building_time)
            if indegree[k] == 0:
                dq.append((k, max(max_times[k]) + building_times[k]))
    # print(result)
    # print(building_times)
    return building_times


if __name__ == '__main__':
    N = int(input()) # 건물의 번호는 1부터 N까지
    relationships = [[] for _ in range(N+1)]

    # solve1(N, relationships)
    answers = solve2(N, relationships)
    for i in range(1, len(answers)):
        print(answers[i])

