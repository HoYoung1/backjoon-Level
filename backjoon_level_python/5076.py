def solve(input_text):
    stack = []

    temp = ''
    tag_on_off = False
    for s in input_text:
        if tag_on_off is False and s == ' ':
            continue

        if tag_on_off is True and (s == ' ' or s == '>'):
            tag_on_off = False
            if temp == 'br':
                temp = ''
                continue
            if temp and temp[0] == '/':
                # 닫는 태그
                if stack and stack[-1] == temp[1:]:
                    stack.pop()
                    temp = ''
                    continue

                else:
                    return 'illegal'
            stack.append(temp)
            temp = ''

        if tag_on_off is True:
            temp += s

        if s == '<':
            tag_on_off = True
    if stack:
        return 'illegal'
    return 'legal'



if __name__ == '__main__':
    while True:
        input_text = input()
        if input_text == '#':
            break
        print(solve(input_text))