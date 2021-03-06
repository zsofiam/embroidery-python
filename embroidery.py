def draw_base_matrix(width, height, color):
    matrix = [[color for column in range(width)] for row in range(height)]
    return matrix


def fill_matrix(matrix, row_start, row_end, column_start, column_end, color):
    for row in range(row_start, row_end):
        for column in range(column_start, column_end):
            matrix[row][column] = color
    return matrix


def draw_rectangle(width, height, border_color=1, fill_color=1, border_width=1):
    if width < 1 or height < 1 or border_color not in [0,1,2] or fill_color not in [0,1,2] or border_width > width or border_width > height:
        raise ValueError("Error: Incorrect parameter given! Cannot draw rectangle!")
    matrix = draw_base_matrix(width, height, border_color)
    fill_matrix(matrix, border_width, height-border_width, border_width, width-border_width, fill_color)
    return matrix


def draw_triangle(height, border_color=1, fill_color=1):
    if height < 1 or border_color not in [0,1,2] or fill_color not in [0,1,2]:
        raise ValueError("Error: Incorrect parameter given! Cannot draw triangle!")
    width = height * 2 - 1
    matrix = draw_base_matrix(width, height, 0)
    for row in range(height):
        for column in range(height-row-1, width-(height-row-1)):
            matrix[row][column] = border_color
    for row in range(1, height-1):
        for column in range(height-row, width-(height-row)):
            matrix[row][column] = fill_color
    return matrix


def draw_christmas_tree(blocks, border_color=1, fill_color=1):
    if blocks < 1 or border_color not in [0,1,2] or fill_color not in [0,1,2]:
        raise ValueError("Error: Incorrect parameter given! Cannot draw Christmas tree!")
    height = blocks * 3
    width = blocks * 2 + 3
    matrix = draw_base_matrix(width, height, 0)
    start_place = blocks + 2
    count = 3
    for row in range(height):
        if row % 3 == 0:
            start_place -= 1
            count -= 2
        else:
            count += 2
        modify_start_place = row % 3
        for i in range(count):
            if i == 0 or i == count - 1:
                matrix[row][start_place - modify_start_place + i] = border_color
            else:
                matrix[row][start_place - modify_start_place + i] = fill_color
        if row == height - 1:
            for i in range(width):
                matrix[row][i] = border_color
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
    #embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)
    #embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)
    #embroider(draw_rectangle(27, 6, 1, 2, 1), color_scheme)
    embroider(draw_triangle(10, 1, 2), color_scheme)
    embroider(draw_christmas_tree(8, 1, 2), color_scheme)
