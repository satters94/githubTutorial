import numpy as np
import pandas as pd


def my_func(matrix_1, matrix_2):
    try:
        return matrix_1 * matrix_2
    except ValueError:
        print("Matrices are not aligned")
        return None

my_matrix = np.eye(8)
my_second_matrix = np.random.rand(3,3)
print(my_func(my_matrix, my_second_matrix))
