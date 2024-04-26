"""

This script demonstrates the behavior of the `sum()` function from both Python's built-in `sum()` and NumPy.

"""

# Using Python's built-in sum() function sums the values in the range(5) and adds -2 to the result
result1 = sum(range(5), -2)
print("Using Python's built-in sum() function:", result1)

from numpy import *

# The NumPy sum() function sums the values in the range(5) along the last axis (-1)
result2 = sum(range(5), -1)
print("Using NumPy's sum() function:", result2)

# Example 3: Using NumPy's sum() function with a 2D array
array_2d = array([[1, 2, 3], [4, 5, 6]])

# Summing the elements along the last axis (-1) of the 2D array
result3 = sum(array_2d, -1)
print("Summing along the last axis of a 2D array:", result3)
