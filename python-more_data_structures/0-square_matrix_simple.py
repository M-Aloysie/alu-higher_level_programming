#!/usr/bin/python3
# A function that computes the square value of all integers of a matrix


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x ** 2, matrix[i])))
    return new_matrix
