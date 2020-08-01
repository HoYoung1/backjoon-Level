import sys
input = sys.stdin.readline

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def solve(finding_stars, existing_stars):
    # finding_stars.sort()
    # existing_stars.sort()

    # print_matrix(finding_stars)
    # print_matrix(existing_stars)
    for i in range(n):
        x1, y1 = existing_stars[i]
        x2, y2 = finding_stars[0]

        d_x, d_y = x1-x2, y1-y2
        # print('d_x, d_y',d_x, d_y)
        for j in range(m):
            t_x, t_y = finding_stars[j]
            if [t_x + d_x, t_y + d_y] not in existing_stars:
                break
        else:
            break
    return '{} {}'.format(d_x, d_y)




if __name__ == '__main__':
    m = int(input())
    finding_stars = [list(map(int, input().split())) for i in range(m)]

    n = int(input())
    existing_stars = set(list(map(int, input().split())) for i in range(n))
    
    print(solve(finding_stars, existing_stars))
        