print("\nStep 1: Installation and Setup")
# pip install numpy
import numpy as np

# Create NumPy Array from a python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)

# ------------------------------------------------------ #

print("\nStep 2: Array Initialization and Basic Operations")
# Creating arrays of different shapes and initialization methods
zeros_array = np.zeros((3, 3), dtype=int)
ones_array = np.ones((2, 4))
range_array = np.arange(1, 11, 1)
print(zeros_array)
print(ones_array)
print(range_array)

# ------------------------------------------------------ #

print("\nTask 1:")
# Create a 2D array of shape (3, 5) filled with random integer values ranging from 1 to 100 using the np.random.randint() function.
random_array = np.random.randint(1, 101, (3, 5))
print(random_array)

rg = np.random.default_rng()
random_array = rg.integers(1, 101, (3, 5))
print(random_array)

# ------------------------------------------------------ #

print("\nStep 4: Array Indexing and Slicing")
# Indexing and slicing of NumPy arrays
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array[0, 1])  # Accessing a specific element
print(my_array[:, 1])  # Accessing a specific column
print(my_array[1:, :2])  # Accessing a subarray

# Manipulation using slicing
print(my_array)

my_array[0, 1] = 22
my_array[0, :] = [11, 22, 33]  # Assigning a new row to Row 0
my_array[:, 1] = [22, 55, 88]  # Assigning a new column to Column 1

print(my_array)

# ------------------------------------------------------ #

print("\nTask 2:")
# Given a 2D array, extract the last column using slicing.
print(my_array[:, -1])

# ------------------------------------------------------ #

print("\nStep 5: Array Operations and Mathematical Functions")
# Array operations and mathematical functions
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
result = array_1 + array_2  # Element-wise addition
print(result)
result = np.sin(array_1)  # Applying sin() function element-wise
print(result)

# ------------------------------------------------------ #

print("\nTask 3:")
# Given two arrays a = np.array([2, 4, 6]) and b = np.array([1, 3, 5]), calculate the element-wise product of a and b.
a = np.arange(2, 7, 2)  # [2 4 6]
b = np.arange(1, 6, 2)  # [1 3 5]
print(a)
print(b)
product = a * b
mat_product = np.matmul(a, b) # a @ b -> @ stands for Matrix Multiplication
print(product)
print(mat_product)

# ------------------------------------------------------ #

print("\nStep 6: Array Aggregations and Statistical Operations")
# Array aggregations and statistical operations
my_array = np.array([1, 2, 3, 4, 5])
print(np.sum(my_array))             # Sum of all elements
print(np.mean(my_array))            # Mean of all elements
print(np.min(my_array))             # Minimum value
print(np.max(my_array))             # Maximum value
print(np.std(my_array))             # Standard deviation

# ------------------------------------------------------ #

print("\nTask 4:")
# Given an array data = np.array([7, 9, 11, 13, 15]), calculate the range (difference between the maximum and minimum values) and the median.

np_arr = np.array([7, 9, 11, 13, 15])
data_range = np.max(np_arr) - np.min(np_arr)
print("Range:", data_range)
print("Median:", np.median(np_arr))

# ------------------------------------------------------ #

