'''
Function to run gaussian elimination
'''

import numpy as np
from functions import *

def gaussian_elimination_function(A, b):

    row_echelon_M = row_echelon_form(A, b)

    if type(row_echelon_M) == str:
        return row_echelon_M
    
    solution = back_substitution(row_echelon_M)

    return solution

A = np.array([[1, 2, 10], [4, 5, 6], [7, 8, 9]])
B = np.array([[1], [2], [3]])
print(gaussian_elimination_function(A, B))