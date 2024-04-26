"""

This script demonstrates the creation of a diagonal matrix using NumPy.

1. Creating a diagonal matrix with values from 1 to 4 shifted to the lower diagonal.

"""

import numpy as np

# Creating a diagonal matrix with values from 1 to 4 shifted to the lower diagonal
a = np.diag(np.arange(1, 5), k=-1)
print("Diagonal Matrix (a):\n", a)

# Creating a 5x5 matrix
b = np.arange(0, 25).reshape(5, 5)
print("Original Matrix (b):\n", b)

# Extracting the diagonal elements from the 5x5 matrix
print("Diagonal Elements of Matrix (b):\n", np.diag(b))
