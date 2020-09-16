import sys

input = sys.stdin.readline

def solve(num):
    # half = num//2
    half = num
    answer = 'IMPOSSIBLE'
    for idx in range(half, 0, -1):
        for i in range(idx-2, -1, -1):
            if l[idx] - l[i] == num:
                # answer
                answer = '{} = '.format(num)
                for j in range(i+1, idx+1):
                    answer += str(j) + ' '
                    if j != idx:
                        answer += '+ '
            elif l[idx] - l[i] > num:
                break
    return answer
    

if __name__ == '__main__':
    l = [0]
    i = 1
    while True:
        num = l[-1] + i
        if num > 10**9:
            break
        l.append(num)
        i += 1
    # print(l)

    T = int(input())
    for i in range(T):
        print(solve(int(input())))