import numpy as np
import pandas as pd

my_matrix = np.eye(5)
my_second_matrix = np.random.rand(5,4)
print(my_second_matrix.dot(my_matrix))
