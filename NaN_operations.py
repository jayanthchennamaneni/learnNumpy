"""

This script demonstrates various operations involving NaN (Not a Number) using NumPy.

1. Performing arithmetic operations involving NaN.
2. Comparing NaN values.
3. Checking if NaN is present in a set.

"""

import numpy as np

# Performing arithmetic operations involving NaN
print("0 * NaN:", 0 * np.nan)
print("NaN - NaN:", np.nan - np.nan)
print("NaN + NaN:", np.nan + np.nan)

# Comparing NaN values
print("NaN == NaN:", np.nan == np.nan)

# Checking if NaN is present in a set
print("NaN in set([1, 2, NaN]):", np.nan in set([1, 2, np.nan]))

