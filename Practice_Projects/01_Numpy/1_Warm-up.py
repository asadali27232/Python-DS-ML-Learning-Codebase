import numpy as np

# Step 1: Installation and Setup
# pip install numpy
# Create NumPy Array from a python list
my_list = [1, 2, 3, 4, 5]
my_aaray = np.array(my_list)
print(my_aaray)


# Step 2: Array Initialization and Basic Operations
# Creating arrays of different shapes and initialization methods
zeros_array = np.zeros((3, 3), dtype=int)
ones_array = np.ones((2, 4))
range_array = np.arange(1, 11, 1)
print(zeros_array)
print(ones_array)
print(range_array)


# Task 1:
# Create a 2D array of shape (3, 5) filled with random integer values ranging from 1 to 100 using the np.random.randint() function.
random_array = np.random.randint(1, 101, (3, 5))
print(random_array)

rg = np.random.default_rng()
random_array = rg.integers()(1, 101, (3, 5))
print(random_array)


# Step 4: Array Indexing and Slicing



