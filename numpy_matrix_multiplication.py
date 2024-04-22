"""

This script demonstrates the usage of matrix multiplication in NumPy using both np.dot() and the '@' operator.

"""

import numpy as np

# Example 1: Matrix multiplication using np.dot()
a = np.ones((4, 3))
b = np.ones((3, 5))

c = np.dot(a, b)
print("Matrix Multiplication using np.dot():\n", c)

# Example 2: Matrix multiplication using the '@' operator
d = a @ b
print("\nMatrix Multiplication using '@' operator:\n", d)

# Matrix multiplication with different shapes
e = np.ones((2, 3))
f = np.ones((3, 2))
g = e @ f
print("Matrix Multiplication with Different Shapes (2x3 @ 3x2):\n", g)

# Matrix multiplication with identity matrix
identity = np.eye(3)
result = a @ identity
print("Matrix Multiplication with Identity Matrix (4x3 @ 3x3):\n", result)
