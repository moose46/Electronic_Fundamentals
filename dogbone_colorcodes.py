COLOR_CODES = ["BLACK", "BROWN", "RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "VIOLET", "GRAY", "WHITE"]
BLACK = 0
BROWN = 1
RED = 2
ORANGE = 3
YELLOW = 4
GREEN = 5
BLUE = 6
VIOLET = 7
GRAY = 8
WHITE = 9


def get_color_codes(value: [float | int]):
    print(value, end=' = ')
    str_value = str(int(value))

    pos = 0
    # print the first color, used on the body of the resistor
    print(COLOR_CODES[int(str_value[pos])], end=' ')
    pos += 1
    # print the second color
    #    if int(str_value[pos]) != 0:
    print(COLOR_CODES[int(str_value[pos])], end=' ')
    pos += 1
    if value < 100:
        print(COLOR_CODES[BLACK], end=' ')
    elif value < 1000:
        print(COLOR_CODES[BROWN], end=' ')
    elif value < 10000:
        print(COLOR_CODES[RED], end=' ')
    elif value < 100000:
        print(COLOR_CODES[ORANGE], end=' ')
    elif value < 1e6:
        print(COLOR_CODES[YELLOW], end=' ')
    elif value < 10000000:
        print(COLOR_CODES[GREEN], end=' ')
    elif value < 100000000:
        print(COLOR_CODES[BLUE], end=' ')
    print()


get_color_codes(10)
get_color_codes(25)
get_color_codes(300)
get_color_codes(560)
get_color_codes(3000)
get_color_codes(5400)
get_color_codes(10000)
get_color_codes(62000)
get_color_codes(200000)
get_color_codes(430000)
get_color_codes(3000000)
get_color_codes(6700000)
get_color_codes(18000000)
get_color_codes(20000000)
