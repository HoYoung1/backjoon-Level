import sys
sys.setrecursionlimit(10000)

break_flag = False


def get_edges_from_input():
    input_data = ''

    while True:
        input_data += input()

        if input_data[-3:] == '0 0':
            input_data = input_data[:-3]
            break
        else:
            input_data += ' '
    return input_data.split()


def find_parent(value):
    if value not in parents:
        return value
    return find_parent(parents[value])


if __name__ == '__main__':
    count = 0
    while True:
        count += 1

        edges = get_edges_from_input()

        if not edges:
            print('Case {} is a tree.'.format(count)) # 0 0 트리
            # if input() == '-1 -1':
            #     break
            # continue
        else:
            parents = {}

            # break_flag = False
            for i in range(0, len(edges), 2):
                if edges[i+1] in parents:
                    print('Case {} is not a tree.'.format(count))
                    # break_flag = True
                    break
                else:
                    parents[edges[i+1]] = edges[i]
            else:
                print('parents {} '.format(parents))

                root = find_parent(list(parents.values())[0])
                for key, value in parents.items():
                    parent = find_parent(key) # parent가 다 root 로 같아야함
                    parents[key] = parent
                    if root != parent:
                        print('Case {} is not a tree.'.format(count))
                        break
                else:
                    print('Case {} is a tree.'.format(count))
        if input() == '-1 -1':
            break
        else:
            continue









