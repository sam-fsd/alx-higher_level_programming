#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    dlmtr = ' '
    for row in matrix:
        print(dlmtr.join("{:d}".format(element) for element in row))
