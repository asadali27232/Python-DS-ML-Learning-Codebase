import numpy as np
import matplotlib.pyplot as plt

# Task 1: Reading and writing image in and from numpy array
me = plt.imread("images/pic.jpeg")

print(me.max())

me_90 = np.rot90(me)
plt.imsave("images/pic.png", me_90)
