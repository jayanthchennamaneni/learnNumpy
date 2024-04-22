"""
numpy_array_operations.py

This script demonstrates various array operations using NumPy.

1. Creating a 1D array using arange() function.
2. Reversing the array using slicing.
3. Creating a 2D array using arange() and reshape() functions.
4. Performing element-wise addition on the 2D array.


"""
import numpy as np  # Importing NumPy library and aliasing it as np

# Creating a 1D array using arange() function
a = np.arange(3, 45)
print("1D Array (a):", a)

# Reversing the array using slicing
b = a[::-1]
print("Reversed Array (b):", b)

# Creating a 2D array using arange() and reshape() functions
c = np.arange(1, 10).reshape(3, 3)
print("2D Array (c):\n", c)

# Performing element-wise addition on the 2D array
c += 1
print("Modified 2D Array (c + 1):\n", c)
