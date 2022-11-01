#!/usr/bin/python3
# Printing a matrix of integers

def print_matrix_integer(matrix=[[]]):
    For row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
