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
# plt.waitforbuttonpress()

# ------------------------------------------------------------------- #

# Task 1: Convert Images to same dimensions 2500 x 2000
butterfly1 = plt.imread("images/Butterflies/butterfly1.jpg")
butterfly2 = plt.imread("images/Butterflies/butterfly2.jpg")
butterfly3 = plt.imread("images/Butterflies/butterfly3.jpg")

plt.subplots(1, 3, figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(butterfly1)
plt.title(f"({butterfly1.shape[0]}x{butterfly1.shape[1]})")

plt.subplot(1, 3, 2)
plt.imshow(butterfly2)
plt.title(f"({butterfly2.shape[0]}x{butterfly2.shape[1]})")

plt.subplot(1, 3, 3)
plt.imshow(butterfly3)
plt.title(f"({butterfly3.shape[0]}x{butterfly3.shape[1]})")

plt.suptitle("Images with Different Dimensions", fontsize=16)
plt.waitforbuttonpress()

# Croping
butterfly1 = butterfly1[:2500, :2000, :]
butterfly2 = butterfly2[:2500, :2000, :]
butterfly3 = butterfly3[:2500, :2000, :]

plt.subplot(1, 3, 1)
plt.imshow(butterfly1)
plt.title(f"({butterfly1.shape[0]}x{butterfly1.shape[1]})")

plt.subplot(1, 3, 2)
plt.imshow(butterfly2)
plt.title(f"({butterfly2.shape[0]}x{butterfly2.shape[1]})")

plt.subplot(1, 3, 3)
plt.imshow(butterfly3)
plt.title(f"({butterfly3.shape[0]}x{butterfly3.shape[1]})")

plt.suptitle("Images Croped to Same Deimensions")
plt.waitforbuttonpress()

# ------------------------------------------------------------------- #

# Task 2: Convert Image to Grayscale
avg_color_b1 = np.average(butterfly1, axis=2)
avg_color_b2 = np.average(butterfly2, axis=2)
avg_color_b3 = np.average(butterfly3, axis=2)

copy_b1 = np.copy(butterfly1)
copy_b2 = np.copy(butterfly2)
copy_b3 = np.copy(butterfly3)

copy_b1[..., 0] = avg_color_b1
copy_b1[..., 1] = avg_color_b1
copy_b1[..., 2] = avg_color_b1

copy_b2[..., 0] = avg_color_b2
copy_b2[..., 1] = avg_color_b2
copy_b2[..., 2] = avg_color_b2

copy_b3[..., 0] = avg_color_b3
copy_b3[..., 1] = avg_color_b3
copy_b3[..., 2] = avg_color_b3


plt.subplot(1, 3, 1)
plt.imshow(copy_b1)

plt.subplot(1, 3, 2)
plt.imshow(copy_b2)

plt.subplot(1, 3, 3)
plt.imshow(copy_b3)

plt.suptitle("Images Converted to Gray Scale")
plt.waitforbuttonpress()
