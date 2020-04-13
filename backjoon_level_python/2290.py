
def init_lcd_number(s):
    # init
    lcd_number = {}
    for i in range(10):
        lcd_number[i] = []

    EMPTY = " " * (s + 2) + " "
    HORIZON = " " + "-" * s + " " + " "
    VERTICAL_LEFT = "|" + " " * (s + 1) + " "
    VERTICAL_RIGHT = " " * (s + 1) + "|" + " "
    VERTICAL_LEFT_RIGHT = "|" + " " * s + "|" + " "

    number = 0
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(EMPTY)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)

    number = 1
    lcd_number[number].append(EMPTY)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(EMPTY)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(EMPTY)

    number = 2
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT)
    lcd_number[number].append(HORIZON)

    number = 3
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(HORIZON)

    number = 4
    lcd_number[number].append(EMPTY)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(EMPTY)

    number = 5
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(HORIZON)

    number = 6
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)

    number = 7
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(EMPTY)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(EMPTY)

    number = 8
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)

    number = 9
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_LEFT_RIGHT)
    lcd_number[number].append(HORIZON)
    for _ in range(s):
        lcd_number[number].append(VERTICAL_RIGHT)
    lcd_number[number].append(HORIZON)

    return lcd_number


if __name__ == '__main__':
    s, n = input().split()
    s = int(s)

    _, column = s + 2, 2 * s + 3

    lcd_number = init_lcd_number(s)

    lcd_board = []
    for col in range(column):
        line = ""
        for number in n:
            line += lcd_number[int(number)][col]
        lcd_board.append(line)

    for row in lcd_board:
        print(row)
