#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    i = 0

    while i < matrix_len:
        row_len = len(matrix[0])
        j = 0
        
        while j < row_len:
            print("{:d}".format(matrix[i][j]), end=' ')
            j += 1
        
        print()
        i += 1
