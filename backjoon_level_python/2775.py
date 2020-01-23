matrix = []
temp = []
for i in range(0,15,1):
    temp.append(i)
matrix.append(temp)
# print(matrix)

for i in range(1,15):
    templist = []
    for j in range(15):
        if j == 0:
            temp = matrix[i-1][0]
        else:
            temp = matrix[i-1][j] + templist[j-1]
        templist.append(temp)
    matrix.append(templist)
# print(matrix)


def solution(k, n):
    return matrix[k][n]


if __name__ == '__main__':
    for i in range(int(input())):
        k = int(input())
        n = int(input())
        answer = solution(k, n)
        print(answer)