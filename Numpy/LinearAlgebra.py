import numpy as np


# Task 1: Matrix Addition
print("\nTask 1:")


def matrix_adder(*matrices):
    if not matrices:
        raise ValueError("At least one matrix must be provided.")

    shape = matrices[0].shape
    for matrix in matrices:
        if matrix.shape != shape:
            raise ValueError("All input matrices must have the same shape.")

    result = np.zeros(matrices[0].shape)
    for matrix in matrices:
        result = np.add(result, matrix)
    return result


A = np.random.randint(1, 100, (200, 200))
B = np.random.randint(1, 100, (200, 200))
C = np.random.randint(1, 100, (200, 200))

result = matrix_adder(A, B, C)
print(result)

# ----------------------------------------------------------------- #

# Task 2: Matrix Subtraction
print("\nTask 2:")


def matrix_subtracter(*matrices):
    if not matrices:
        raise ValueError("At least one matrix must be provided.")

    shape = matrices[0].shape
    for matrix in matrices:
        if matrix.shape != shape:
            raise ValueError("All input matrices must have the same shape.")

    for i, matrix in enumerate(matrices):
        if i == 0:
            result = matrix
        else:
            result = np.subtract(result, matrix)

    return result


A = np.random.randint(1, 100, (200, 200))
B = np.random.randint(1, 100, (200, 200))
C = np.random.randint(1, 100, (200, 200))

print(matrix_subtracter(A, B, C))

# ----------------------------------------------------------------- #

# Task 3: Matrix Multiplication
print("\nTask 3:")


def matrix_multiplier(*matrices):
    if not matrices:
        raise ValueError("At least one matrix must be provided.")

    for i, matrix in enumerate(matrices):
        if i == 0:
            result = matrix
        elif result.shape[1] != matrix.shape[0]:
            raise ValueError(f"Matrix {i+1} is not capible to be multiplied with the previous result.")
        else:
            result = result @ matrix
    return result


A = np.array([[1], [2]])
B = np.array([[1, 3]])

print(matrix_multiplier(A, B))

# ----------------------------------------------------------------- #

# Task 4: Matrix Transpose
print("\nTask 4:")

A = np.array([[1, 2, 3], [4, 5, 6]])
A_T = A.T
print(A, A_T, sep="\n")

# ----------------------------------------------------------------- #

# Task 5: Matrix Inverse
print("\nTask 5:")


def matrix_inverser(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Provided matrix must be a square matrix")
    elif np.linalg.det(matrix) == 0:
        raise ValueError("Determinent of the provided matrix must be 0")
    else:
        return np.linalg.inv(matrix)


A = np.array([[1, 9, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_inverser(A))

# ----------------------------------------------------------------- #

# Task 6: Determinant and Eigenvalues
print("\nTask 6:")

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A_det = np.linalg.det(A)
print(A_det)

A_EgVal = np.linalg.eigvals(A)
print(A_EgVal)

# ----------------------------------------------------------------- #
