import numpy as np

my_matrix = np.eye(4)

my_second_matrix = np.random.rand(4,4)

print(my_second_matrix.dot(my_matrix))
