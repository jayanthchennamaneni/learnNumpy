"""

This script demonstrates various array creation and manipulation operations using NumPy.

1. Creating a 1D array of ones with 3 elements.
2. Creating a 4x4 array of ones.
3. Setting inner elements of a 4x4 array to zero.
4. Creating an array of ones with the same shape as another array.
5. Padding a 5x5 array of ones with zeros around the edges.
6. Setting the first and last rows and columns of a 5x5 array to zero.

"""

import numpy as np

# Creating a 1D array of ones with 3 elements
a = np.ones(3)
print("1D Array of Ones (a):", a)

# Creating a 4x4 array of ones
b = np.ones((4, 4))
print("4x4 Array of Ones (b):\n", b)

b[1:-1, 1:-1] = 0  # Setting inner elements of a 4x4 array to zero
print("Modified Array with Inner Elements Zeroed (b):\n", b)

# Creating an array of ones with the same shape as another array
c = np.zeros((3,2))
d = np.ones_like(c)
print("Array of Ones with Same Shape as 'c' (d):\n", d)

# Padding a 5x5 array of ones with zeros around the edges
e = np.ones((5,5))
f = np.pad(e, pad_width=1, constant_values=0, mode='constant')
print("Padded Array (f):\n", f)

# Setting the first and last rows and columns of a 5x5 array to zero
e[:, [0,-1]] = 0
e[[0,-1], :] = 0
print("Array with First and Last Rows and Columns Zeroed (e):\n", e)
