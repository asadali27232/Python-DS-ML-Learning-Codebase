# Import numpy package
import numpy as np

# Collapse the data lists to view main code
baseball = [
    [74, 180],
    [74, 215],
    [72, 210],
    [72, 210],
    [73, 188],
    [69, 176],
    [69, 209],
    [71, 200],
    [76, 231],
    [71, 180],
    [73, 188],
    [73, 180],
    [74, 185],
    [74, 160],
    [69, 180],
    [70, 185],
    [73, 189],
    [75, 185],
    [78, 219],
    [79, 230],
    [76, 205],
    [74, 230],
    [76, 195],
    [72, 180],
    [71, 192],
    [75, 225],
    [77, 203],
    [74, 195],
    [73, 182],
    [74, 188],
    [78, 200],
    [73, 180],
    [75, 200],
    [73, 200],
    [75, 245],
    [75, 240],
    [74, 215],
    [69, 185],
    [71, 175],
    [74, 199],
    [73, 200],
    [73, 215],
    [76, 200],
    [74, 205],
    [74, 206],
    [70, 186],
]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
