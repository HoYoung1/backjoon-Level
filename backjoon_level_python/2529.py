def dfs(depth, idx, temp):
    if depth == len(inequality_signs) + 1:
        valid_list.append(temp)
    else:
        for i in range(0, len(number_list)):
            if visited[i]:
                continue
            else:
                if inequality_signs[depth - 1] == '<' and number_list[idx] < number_list[i]:
                    dive_dfs(depth, i, temp)
                elif inequality_signs[depth - 1] == '>' and number_list[idx] > number_list[i]:
                    dive_dfs(depth, i, temp)


def dive_dfs(depth, i, temp):
    visited[i] = True
    temp += str(number_list[i])
    dfs(depth + 1, i, temp)
    visited[i] = False


def solution():
    depth = 0
    for idx, number in enumerate(number_list):
        visited[idx] = True
        dfs(depth + 1, idx, str(number))
        visited[idx] = False

    return valid_list[-1], valid_list[0]


if __name__ == '__main__':
    _ = input()
    inequality_signs = input().split()
    number_list = [i for i in range(10)]
    visited = [False] * len(number_list)
    valid_list = []

    maximum, minimum = solution()
    print(maximum)
    print(minimum)
