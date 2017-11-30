from utils.utils import f_to_str


def print_named(name, value):
    print(name)
    print(value)
    print()


def print_equations(matrix, right_side, variables):
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    result = ''

    for row in range(0, rows):
        line = ''
        for col in range(0, cols):
            num = matrix[row][col]
            variable = variables[col]
            if col == 0:
                if num < 0:
                    line += f'{f_to_str(num)} {variable}'
                else:
                    line += f' {f_to_str(num)} {variable}'
            else:
                if num < 0:
                    line += f' - {f_to_str(num * -1)} {variable}'
                else:
                    line += f' + {f_to_str(num)} {variable}'

        line += f' = {f_to_str(right_side[row])}'
        result += f'{line}\n'
    print(result)


def print_solution(solution, variables):
    rows = solution.shape[0]
    result = 'solution: '
    for row in range(0, rows):
        if row != 0:
            result += ', '
        result += f'{variables[row]} = {f_to_str(solution[row])}'

    print(result)
