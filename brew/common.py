def lfill(s, width):
    if len(s) > width:
        s = s[:width]
    return ' ' * (width - len(s)) + s


def rfill(s, width):
    if len(s) > width:
        s = s[:width]
    return s + ' ' * (width - len(s))


def slider(label, minval, maxval, val, fmt):
    tick = (maxval - minval) / 40.0
    pos = int((val - minval) / tick)
    print('  ', rfill(label, 3), rfill(fmt % val, 6),
          rfill(fmt % minval, 6), end='')
    for i in range(-5, 45):
        if i == pos:
            print('X', end='')
        elif i in (0, 39):
            print('|', end='')
        else:
            print('-', end='')
    print(' ', fmt % maxval)
