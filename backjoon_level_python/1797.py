import sys
input = sys.stdin.readline

def solve(matrix, N):
    answer = -1
    matrix.sort(key=lambda x: x[1])
    s = [0] * N


    for idx, (sex, location) in enumerate(matrix):
        s[idx] = s[idx-1] + sex
    s[0] = matrix[0][0]

    # print(s)

    dict = {}
    for idx, ss in enumerate(s):
        if ss in dict:
            dict[ss]['right'] = matrix[idx][1]
        else:
            if idx+1 < len(matrix):
                dict[ss] = {
                    'left': matrix[idx+1][1]
                }

    # print(dict)
    max_length = 0
    for key in dict:
        if 'left' in dict[key] and 'right' in dict[key]:
            max_length = max(max_length, dict[key]['right'] - dict[key]['left'])
    # print(max_length)

    answer = max_length
    if len(matrix) == 2 and matrix[1][0] != matrix[0][0]:
        answer = matrix[1][1]-matrix[0][1]

    return answer


if __name__ == '__main__':
    N = int(input().rstrip())
    matrix = []
    for i in range(N):
        sex, location = map(int, input().rstrip().split())
        if sex == 0:
            sex = -1
        matrix.append((sex, location))



    print(solve(matrix, N))