import sys
# input = sys.stdin.readline

if __name__ == '__main__':

    dic = {}
    count = 0
    try:
        for i in range(29):
            a = input()
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
            count += 1
    except:
        pass
    # exit()
    # print(1)
    for key in sorted(dic.keys()):
        # print(key)
        print('{} {:.4f}'.format(key, (dic[key]/count) * 100))