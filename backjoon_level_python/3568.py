if __name__ == '__main__':
    variables_line = input()
    variables = variables_line.split()
    variable_type, variables = variables[0], variables[1:]

    for variable in variables:
        variable_length = len(variable)-1
        for idx, s in enumerate(variable):
            if s in '&[]*':
                variable_length = idx
                break

        print(variable_type, end="")
        for s in variable[variable_length:-1][::-1]:
            if s == '[':
                print(']', end="")
            elif s == ']':
                print('[', end="")
            else:
                print(s, end="")
        print(' '+variable[:variable_length]+";")
