"""
This script demonstrates the creation of identity matrices using NumPy.

1. Creating a 3x3 identity matrix.
2. Creating a 3x3 identity matrix with a shift along the diagonal.
3. Creating a 4x4 identity matrix with a shift along the diagonal.
4. Creating a 4x3 identity matrix with a specified shape and shift along the diagonal.

"""

import numpy as np

# Creating a 3x3 identity matrix
a = np.eye(3)
print("Identity Matrix (a):\n", a)

# Creating a 3x3 identity matrix with a shift along the diagonal
b = np.eye(3, k=1)
print("Identity Matrix with Shift (b):\n", b)

# Creating a 4x4 identity matrix with a shift along the diagonal
c = np.eye(4, k=-1)
print("Identity Matrix with Negative Shift (c):\n", c)

# Creating a 4x3 identity matrix with a specified shape and shift along the diagonal
d = np.eye(4, 3, 1)
print("Identity Matrix with Custom Shape and Shift (d):\n", d)
