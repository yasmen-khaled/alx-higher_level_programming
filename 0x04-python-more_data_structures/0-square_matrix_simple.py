#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mat = matrix.copy()

    for x in range(len(matrix)):
        mat[x] = list(map(lambda j: j**2, matrix[x]))

    return (mat)
