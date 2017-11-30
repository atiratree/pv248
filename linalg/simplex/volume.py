import numpy


def volume(*args, round_flag=True, round_to_decimal_places=7):
    length = len(args)
    # 𝑛 + 1 points determine an 𝑛-simplex
    simplex_dimension = length - 1
    if length < 3:
        raise ValueError("there must be at least 3 parameters")
    for point in args:
        if not isinstance(point, list):
            raise ValueError("all parameters must be of type list")
        if len(point) != simplex_dimension:
            raise ValueError("point must be one dimension lower than number of points")
        for num in point:
            if not isinstance(num, (int, float)):
                raise ValueError(f'invalid point #{point}; list must consist of only numbers of type int or float')

    first_point = args[0]
    matrix = []
    # suppose an 𝑛-dimensional space == simplex_dimension
    for point_idx in range(1, length):
        # subtract first_point from all the others and put them into the matrix
        point = args[point_idx]
        result_point = []
        for i in range(0, simplex_dimension):
            result_point.append(point[i] - first_point[i])
        matrix.append(result_point)

    det = numpy.linalg.det(matrix)
    fact = numpy.math.factorial(simplex_dimension)
    simplex_volume = numpy.abs(numpy.divide(det, fact))
    if round_flag:
        simplex_volume = numpy.round(simplex_volume, round_to_decimal_places)
    return simplex_volume
