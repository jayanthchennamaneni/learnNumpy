"""
This script demonstrates various random number generation operations using NumPy.

1. Generating an array of 10 random floats between 0.0 and 1.0.
2. Generating a 10x10 array of random floats between 0.0 and 1.0.
3. Generating an array of 10 random integers between 0 and 9.
4. Displaying the maximum, minimum, and mean values of the integer array.
5. Finding the indices of non-zero elements in the integer array.

"""
import numpy as np

# Generating an array of 10 random floats between 0.0 and 1.0
a = np.random.random(10)
print("Random Floats (a):", a)

# Generating a 10x10 array of random floats between 0.0 and 1.0
a1 = np.random.random((10, 10))
print("Random Floats (a1):\n", a1)

# Generating an array of 10 random integers between 0 and 9
b = np.random.randint(low=0, high=10, size=10)
print("Random Integers (b):", b)

# Displaying the maximum, minimum, and mean values of the integer array
print("Max:", b.max(), "Min:", b.min(), "Mean:", b.mean())

# Finding the indices of non-zero elements in the integer array
print("Indices of Non-Zero Elements:", b.nonzero())
