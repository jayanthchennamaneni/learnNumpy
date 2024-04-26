"""

This script demonstrates various operations on an integer vector using NumPy arrays.

"""

import numpy as np

# Define an integer vector
a = np.array([1, 2, 3, 4])

print("Element-wise exponentiation:")
print(a**a)

print("\nBitwise left shift operation (2 << a):")
print(2 << a)

print("\nBitwise right shift operation (a >> 2):")
print(a >> 2)

print("\nComplex multiplication (1j * a):")
print(1j * a)

print("\nElement-wise division (a/1/1):")
print(a / 1)

print("Absolute value of elements (np.abs(a)):")
print(np.abs(a))

print("Cumulative sum of elements (np.cumsum(a)):")
print(np.cumsum(a))
