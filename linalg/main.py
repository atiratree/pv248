import numpy
from utils import generate_alphabet_variables
from printer import print_equations, print_solution, print_named


def check_args(rows, cols, right_side_rows):
    if rows < 0 or cols < 0 or right_side_rows < 0:
        raise Exception('Unsupported: negative matrix dimension')

    if rows != cols:
        raise Exception('Unsupported: Not a square matrix')

    if rows > right_side_rows:
        raise Exception('Unsupported: not enough right side coefficients')

    if rows < right_side_rows:
        raise Exception('Unsupported: too many right side coefficients')


def run():
    matrix = numpy.loadtxt('matrix.csv', delimiter=",")
    matrix_right_side = numpy.loadtxt('matrix_right_side_coefficients.csv', delimiter=",")

    rows = matrix.shape[0]
    cols = matrix.shape[1]
    right_side_rows = matrix_right_side.shape[0]

    check_args(rows, cols, right_side_rows)

    inverse_matrix = numpy.linalg.inv(matrix)
    det = numpy.linalg.det(matrix)
    solution = numpy.linalg.solve(matrix, matrix_right_side)

    print_named('matrix', matrix)
    print_named('inverse_matrix', inverse_matrix)
    print_named('determinant', det)

    variables = generate_alphabet_variables(cols)
    print_equations(matrix, matrix_right_side, variables)
    print_solution(solution, variables)


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)

