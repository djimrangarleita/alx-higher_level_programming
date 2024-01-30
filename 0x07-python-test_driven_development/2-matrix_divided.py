#!/usr/bin/python3
"""Module with one function to divide a matrix"""


def matrix_divided(matrix, div):
    """Divide members of a matrix by div and return a new matrix"""
    if type(matrix) is not list:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if type(div) is not int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return (divid_matrix(matrix, div))


def divid_matrix(matrix, div):
    """Divid matrix of elts and return"""
    row_size = -1
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                  'matrix must be a matrix (list of lists) of integers/floats')
        if row_size == -1:
            row_size = len(row)
        if row_size != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        for elt in row:
            if type(elt) not in [int, float]:
                raise TypeError(
                 'matrix must be a matrix (list of lists) of integers/floats')
            new_row.append(round(elt/div, 2))
        new_matrix.append(new_row)
    return new_matrix
