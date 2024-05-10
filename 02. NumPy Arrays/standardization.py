"""

This script demonstrates how to standardize a NumPy array by subtracting its mean and dividing by its standard deviation.

"""

import numpy as np

# Generate a random 5x5 array
a = np.random.random((5, 5))

# Standardizing the array 'a' using mean and standard deviation calculated separately
norm_A1 = (a - a.mean()) / a.std()
print("\nStandardized Array (Using Methods):\n", norm_A1)

# Standardizing the array 'a' using NumPy's mean and standard deviation functions
norm_A = (a - np.mean(a)) / np.std(a)
print("\nStandardized Array (Using NumPy Functions):\n", norm_A)
