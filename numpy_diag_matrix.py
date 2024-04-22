"""

This script demonstrates the creation of a diagonal matrix using NumPy.

1. Creating a diagonal matrix with values from 1 to 4 shifted to the lower diagonal.

"""

import numpy as np

# Creating a diagonal matrix with values from 1 to 4 shifted to the lower diagonal
a = np.diag(np.arange(1, 5), k=-1)
print("Diagonal Matrix (a):\n", a)
