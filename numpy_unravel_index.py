"""

This script demonstrates the usage of the np.unravel_index() function in NumPy.

1. Unraveling a flat index to obtain the indices in a multi-dimensional array.

"""

import numpy as np

# Unraveling a flat index to obtain the indices in a 3D array with dimensions (6, 7, 8)
indices = np.unravel_index(99, (6, 7, 8))
print("Indices for Flat Index 99 in a 3D Array (6, 7, 8):", indices)


print("Indices for Flat Index 10 in a 2D Array (5, 2):", np.unravel_index(9, (5, 2)))
print("Indices for Flat Index 40 in a 3D Array (2, 5, 4):", np.unravel_index(20, (2, 5, 4)))
print("Indices for Flat Index 5 in a 1D Array (10,):", np.unravel_index(5, (10,)))
