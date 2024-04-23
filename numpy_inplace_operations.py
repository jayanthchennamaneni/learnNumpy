"""

This script demonstrates how to perform in-place operations on NumPy arrays.

"""

import numpy as np

# Example 1: Performing in-place operation to set elements within a range to 0
a = np.arange(12)
print("Original Array:\n", a)

a[(3 < a) & (8 > a)] = 0
print("\nArray after in-place operation:\n", a)

# Example 2: Performing in-place addition
b = np.array([1, 2, 3, 4, 5])
print("Original Array (b):\n", b)

b += 10  # Add 10 to each element in the array (in-place)
print("\nArray after in-place addition:\n", b)

# Example 3: Performing in-place multiplication
c = np.array([[1, 2], [3, 4]])
print("\nOriginal Array (c):\n", c)

c *= 2  # Multiply each element in the array by 2 (in-place)
print("\nArray after in-place multiplication:\n", c)
