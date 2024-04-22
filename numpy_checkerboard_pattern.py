"""

This script demonstrates the creation of a checkerboard pattern using NumPy.

1. Creating an 8x8 matrix filled with zeros.
2. Setting alternating elements to 1 to create a checkerboard pattern.

"""

import numpy as np

# Creating an 8x8 matrix filled with zeros
a = np.zeros((8, 8), dtype=int)
print("Matrix with Zeros (a):\n", a)

# Setting alternating elements to 1 to create a checkerboard pattern
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print("Checkerboard Pattern (a):\n", a)
