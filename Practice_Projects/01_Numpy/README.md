Lab: Introduction to NumPy

Objective: The objective of this lab is to introduce students to the fundamental concepts and functionalities of NumPy, a powerful library for numerical computing in Python. Through hands-on practice and code examples, students will gain a solid foundation in NumPy's array manipulation, mathematical operations, and data analysis capabilities.

Lab Steps:

Step 1: Installation and Setup As aspiring data scientists, it is essential to have NumPy installed on your machines. If you haven't already, please follow the installation instructions provided. Once installed, import the NumPy library in Python using the `import numpy as np` statement.

Step 2: NumPy Arrays - The Foundation NumPy arrays are at the core of this library. They provide efficient storage and manipulation of large, multi-dimensional datasets. Begin by introducing students to the concept of NumPy arrays, emphasizing their advantages over regular Python lists, such as improved performance and convenience. Demonstrate the creation of NumPy arrays using the `np.array()` function.

Code Example:

pythonCopy code

`import numpy as np  # Creating a NumPy array from a Python list my_list = [1, 2, 3, 4, 5] my_array = np.array(my_list) print(my_array)`

Step 3: Array Initialization and Basic Operations Guide students through various methods of array initialization and demonstrate basic array operations. Show examples of creating arrays filled with zeros or ones using `np.zeros()` and `np.ones()`. Introduce the `np.arange()` function for creating arrays with regularly spaced values. Encourage students to experiment with different parameters and shapes.

Code Example:

pythonCopy code

`import numpy as np  # Creating arrays of different shapes and initialization methods zeros_array = np.zeros((3, 3)) ones_array = np.ones((2, 4)) range_array = np.arange(0, 10, 2) print(zeros_array) print(ones_array) print(range_array)`

Tasks:

1.  Create a 1D array of shape (5,) filled with zeros.
2.  Create a 2D array of shape (3, 4) filled with ones.
3.  Create a 1D array containing the numbers from 0 to 9.
4.  Create a 1D array containing the odd numbers from 1 to 10.

Step 4: Array Indexing and Slicing Demonstrate how to access and manipulate individual elements, rows, columns, and subarrays of NumPy arrays using indexing and slicing techniques. Highlight the difference between single brackets (`[]`) for indexing and multiple brackets (`[][]`) for slicing.

Code Example:

pythonCopy code

`import numpy as np  # Indexing and slicing of NumPy arrays my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) print(my_array[0, 1])         # Accessing a specific element print(my_array[:, 1])         # Accessing a specific column print(my_array[1:, :2])       # Accessing a subarray`

Tasks: 5. Given a 2D array `arr`, access and print the element in the second row, third column.

6.  Given a 2D array `arr`, access and print the first column.
7.  Given a 2D array `arr`, access and print a subarray consisting of the first two rows and last two columns.

Step 5: Array Operations and Mathematical Functions Introduce students to basic arithmetic operations and mathematical functions that can be performed on NumPy arrays. Emphasize the convenience of element-wise operations and the availability of mathematical functions like `np.sin()`, `np.cos()`, and `np.exp()`.

Code Example:

pythonCopy code

`import numpy as np  # Array operations and mathematical functions array_1 = np.array([1, 2, 3]) array_2 = np.array([4, 5, 6]) result = array_1 + array_2         # Element-wise addition print(result) result = np.sin(array_1)           # Applying sin() function element-wise print(result)`

Tasks: 8. Given two arrays `a = np.array([1, 2, 3])` and `b = np.array([4, 5, 6])`, calculate the element-wise product of `a` and `b`.

9.  Given an array `x = np.array([1, 2, 3])`, calculate the square of each element and store the result in a new array.
10. Given an array `y = np.array([4, 5, 6])`, calculate the exponential of each element and store the result in a new array.

Step 6: Array Aggregations and Statistical Operations Introduce students to aggregations and statistical operations that can be performed on NumPy arrays, such as finding the sum, mean, minimum, maximum, and standard deviation. Emphasize the versatility and efficiency of these operations.

Code Example:

pythonCopy code

`import numpy as np  # Array aggregations and statistical operations my_array = np.array([1, 2, 3, 4, 5]) print(np.sum(my_array))             # Sum of all elements print(np.mean(my_array))            # Mean of all elements print(np.min(my_array))             # Minimum value print(np.max(my_array))             # Maximum value print(np.std(my_array))             # Standard deviation`

Tasks: 11. Given an array `grades = np.array([85, 92, 78, 90, 88])`, calculate the average grade.

12. Given an array `heights = np.array([175, 160, 180, 165, 170])`, find the tallest person's height.
13. Given an array `prices = np.array([10.99, 8.99, 12.99, 9.99])`, calculate the total price.

Step 7: Broadcasting Introduce students to the concept of broadcasting and how it enables element-wise operations on arrays with different shapes. Provide examples demonstrating how NumPy automatically broadcasts arrays.

Code Example:

pythonCopy code

`import numpy as np  # Broadcasting in NumPy array_1 = np.array([1, 2, 3]) array_2 = np.array([[4], [5], [6]]) result = array_1 + array_2         # Broadcasting the addition operation print(result)`

Tasks: 14. Given a 2D array `arr = np.array([[1, 2, 3], [4, 5, 6]])` and a scalar `n = 2`, multiply `arr` by `n` using broadcasting.

15. Given a 1D array `arr = np.array([1, 2, 3, 4])` and a 2D array `weights = np.array([[0.25], [0.5], [0.75], [1]])`, calculate the weighted sum using broadcasting.

Step 8: Array Manipulation Introduce students to various array manipulation techniques, such as reshaping arrays using `np.reshape()`, concatenating arrays using `np.concatenate()`, and splitting arrays using `np.split()`. Provide small practice tasks to reinforce these concepts.

Code Example:

pythonCopy code

`import numpy as np  # Array manipulation in NumPy my_array = np.array([[1, 2], [3, 4], [5, 6]]) reshaped_array = np.reshape(my_array, (2, 3))           # Reshaping the array print(reshaped_array) concatenated_array = np.concatenate((my_array, my_array), axis=0)   # Concatenating arrays print(concatenated_array)`

Tasks: 16. Given a 1D array `arr = np.array([1, 2, 3, 4, 5, 6])`, reshape it into a 2D array with shape (2, 3).

17. Given two 2D arrays `a = np.array([[1, 2, 3], [4, 5, 6]])` and `b = np.array([[7, 8, 9], [10, 11, 12]])`, concatenate them vertically.
18. Given an array `my_array = np.array([1, 2, 3, 4, 5, 6])`, split it into three equal-sized parts.

Step 9: Conclusion and Recap Recap the key concepts covered in the lab, highlighting the importance of NumPy in scientific computing, data analysis, and machine learning. Reinforce the idea that NumPy arrays form the building blocks for efficient numerical computations.

Additional Resources: Encourage students to explore additional resources, such as the official NumPy documentation, tutorials, and online courses, to further enhance their understanding of NumPy beyond the scope of this lab.

By completing this lab, you will have gained a solid understanding of NumPy's array manipulation, mathematical operations, and statistical computations. These skills will serve as a solid foundation for further exploration and utilization of NumPy in various data science and numerical computing tasks.
