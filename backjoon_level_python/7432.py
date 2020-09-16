def render_directories(depth, directories):
    for d in sorted(directories):
        space = ' ' * depth
        print('{}{}'.format(space, d))
        render_directories(depth + 1, directories[d])


def list_to_object(depth, dir_list) -> dict:
    """
    :param depth:
    :param dir_list: WINNT\SYSTEM32\CONFIG
    :return:
    {
        WINNT: {
            SYSTEM32: {
                CONFIG: {}
            }
        }
    }
    """
    if depth == len(dir_list):
        return {}
    return {
        dir_list[depth]: list_to_object(depth + 1, dir_list)
    }


def make_directory(last_result):
    for idx, dir in enumerate(input_directories):
        if dir in last_result:
            last_result = last_result[dir]
        else:
            last_result[dir] = list_to_object(0, input_directories[idx + 1:])
            break


if __name__ == '__main__':
    N = int(input())
    directories = {}
    for i in range(N):
        path = input()
        input_directories = path.split('\\')

        make_directory(directories)
    render_directories(0, directories)








