

def triangle(n: int):
    space_num = n
    lines = []
    for i in range(1, n + 1):
        space_num -= 1
        line = (" " * space_num) + ("*" * i) + ("*" * (i - 1))
        lines.append(line)
    return lines


def draw_diamond(n: int):
    lines = triangle(n)
    print('\n'.join(lines))
    print('\n'.join(lines[-2::-1]))

draw_diamond(5)
