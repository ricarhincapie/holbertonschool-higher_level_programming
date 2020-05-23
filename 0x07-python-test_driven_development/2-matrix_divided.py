#!/usr/bin/python3
"""This module creates a function that divides
all element of a matrix."""


def matrix_divided(matrix, div):
    """
    Matrix divisor
        :param matrix: type list to be divided
        :param div: divisor for the matrix
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if (len(matrix[0]) + len(matrix[1])) % 2 != 0:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for col in row:
            if type(col) != int and type(col) != float:
                raise TypeError(message)

    if type(div) != int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return new_matrix
