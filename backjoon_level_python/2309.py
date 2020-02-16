def dfs(depth, idx):
    if depth == TRUTH_DWARF_NUM:
        if sum_of_visited_dwarf_height() == TOTAL_DWARF_HEIGHT:
            # 출력 후 종료한다.
            for dwarf, bool in zip(dwarfs, visited):
                if bool:
                    print(dwarf)
            exit(0)
    else:
        for i in range(idx, FALSE_DWARF_NUM):
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


def sum_of_visited_dwarf_height():
    sum = 0
    for dwarf, bool in zip(dwarfs, visited):
        if bool:
            sum += dwarf
    return sum


def solution():
    depth = 0
    idx = 0
    dfs(depth, idx)


if __name__ == '__main__':
    FALSE_DWARF_NUM = 9
    TRUTH_DWARF_NUM = 7
    TOTAL_DWARF_HEIGHT = 100

    dwarfs = [int(input()) for _ in range(FALSE_DWARF_NUM)]
    dwarfs.sort()  # 오름차순으로 출력해야하므로, 그냥 오름차순으로 정렬 후 전체 탐색 수행
    visited = [False] * FALSE_DWARF_NUM
    solution()

