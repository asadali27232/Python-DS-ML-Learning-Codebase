import numpy as np
import matplotlib.pyplot as plt

# Task 0: Reading and writing image in and from numpy array
my_iamge = plt.imread("images/my_image.jpeg")

# Image's pixel information
print(my_iamge.min())
print(my_iamge.max())
print(np.average(my_iamge))
print(my_iamge.shape)
print(np.info(my_iamge))

my_iamge_rot90 = np.rot90(my_iamge)
plt.imsave("images/my_iamge_rot90.png", my_iamge_rot90)

my_iamge_T = np.transpose(my_iamge, (1, 0, 2))
plt.imsave("images/my_iamge_T.png", my_iamge_T)

plt.imshow(my_iamge)
plt.waitforbuttonpress()
