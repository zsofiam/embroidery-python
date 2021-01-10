def draw_rectangle(width, height, border_color=1, fill_color=1, border_width=1):
    if width < 1 or height < 1 or border_color not in [0,1,2] or fill_color not in [0,1,2] or border_width > width or border_width > height:
        raise ValueError("Error: Incorrect parameter given!")
    matrix = [[border_color for column in range(width)] for row in range(height)]
    for row in range(border_width, height - border_width):
        for column in range(border_width, width - border_width):
            matrix[row][column] = fill_color
    return matrix


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)
    embroider(draw_rectangle(6, 6, 1, 2, 1), color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)
