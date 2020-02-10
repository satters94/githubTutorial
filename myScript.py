import numpy as np


def my_func(matrix_1, matrix_2):
    return matrix_1 * matrix_2

my_matrix = np.eye(4)
my_second_matrix = np.random.rand(4,5)

print(my_func(my_matrix, my_second_matrix)
