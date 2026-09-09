import numpy as np

def swap_rows(M, row_1_index, row_2_index): # row_1_index and row_2_index are the indices of rows which are to be swapped, M being the main matrix.

    M[[row_1_index, row_2_index]] = M[[row_2_index, row_1_index]]

    return M # Mn is created an returned so that so we don't change the orginal matrix

def get_index_first_non_zero_value_from_column(M, column, starting_row):

    column_array = M[starting_row:, column]

    for i, value in enumerate(column_array):
        if not np.isclose(value, 0, atol=1e-5): # Numbers like 0.00005 is also considered zero
            index = starting_row + i
            return index

    return -1 # Return -1 is non-zero number is not found.

def get_index_first_non_zero_value_from_row(M, row, augmented=False):

    if augmented == True:
        M = M[:, :-1]

    row_array = M[row]

    for i, value in enumerate(row_array):
        if not np.isclose(value, 0, atol=1e-5):
            return i
    return -1

def augmented_matrix(A, b):
    augmented_matrix_M = np.hstack((A, b))
    return augmented_matrix_M

def row_echelon_form(A, b):
    det_A = np.linalg.det(A)

    if det_A == 0:
        return f"Singular Matrix, either redundant or contradictory"

    A = A.astype('float64')
    B = b.astype('float64')

    num_rows = len(A)

    M = augmented_matrix(A, B)

    for row in range(num_rows):
        pivot_candidate = M[row, row]

        if np.isclose(pivot_candidate, 0) == True:
            first_non_zero_value_from_column = get_index_first_non_zero_value_from_column(M, row, row)

            M = swap_rows(M, row, first_non_zero_value_from_column)

            pivot = M[row, row]

        else:
            pivot = pivot_candidate

        M[row] = 1 / pivot * M[row]

        for j in range(row + 1, num_rows):
            value_below_pivot = M[j, row]

            M[j] = M[j] - value_below_pivot * M[row]

    return M

def back_substitution(M):

    num_rows = M.shape[0]
    for i in reversed(range(num_rows)):

        substitution_row = M[i]

        index = get_index_first_non_zero_value_from_row(M, i, augmented=True)

        for j in range(i):

            row_to_reduce = M[j]

            value = row_to_reduce[index]

            row_to_reduce = row_to_reduce - value * substitution_row

            M[j, :] = row_to_reduce

    solution = M[:, -1]

    return solution







    