"""

This script demonstrates the creation of a checkerboard pattern using NumPy.

1. Creating an 8x8 matrix filled with zeros.
2. Setting alternating elements to 1 to create a checkerboard pattern.
3. This script also demonstrates the usage of the np.tile() function in NumPy to repeat a given array along specified dimensions.
"""

import numpy as np

# Creating an 8x8 matrix filled with zeros
a = np.zeros((8, 8), dtype=int)
print("Matrix with Zeros (a):\n", a)

# Setting alternating elements to 1 to create a checkerboard pattern
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print("Checkerboard Pattern (a):\n", a)


# Using np.tile() to create a checkerboard pattern
b = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print("Checkerboard Pattern (4x4):\n", b)