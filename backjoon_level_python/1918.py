
def solve(input_text):
    result = ''
    stack = []
    priority = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    for s in input_text:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    result += stack.pop()
        elif s in '+-/*':
            while stack and priority[stack[-1]] >= priority[s]:
                result += stack.pop()
            stack.append(s)
        else:
            result += s
    # print(result)
    result += ''.join(reversed(stack))

    return result


if __name__ == '__main__':
    input_text = input()
    print(solve(input_text))