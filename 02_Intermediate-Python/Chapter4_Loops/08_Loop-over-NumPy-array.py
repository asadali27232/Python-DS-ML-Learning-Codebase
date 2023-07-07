# Import numpy as np
import numpy as np

np_height = np.array([74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75, 78, 79])

np_baseball = np.array([[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180], [73, 188], [73, 180], [74, 185], [74, 160], [69, 180], [70, 185], [73, 189], [75, 185], [78, 219], [79, 230]])

# For loop over np_height
for height in np.nditer(np_height):
    print(height, "inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)
