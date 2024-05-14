"""

This script demonstrates various operations on NumPy arrays.

"""

import numpy as np

# np.seterr(divide='raise')

# Creating a NumPy array with a single element
print("Example 1: Creating a NumPy array with a single element")
print(np.array(0))

# Performing division on arrays containing zero
print("\nExample 2: Performing division on arrays containing zero")
print(np.array(0) / np.array(0))


'''
both operands are zero, and division by zero is undefined in mathematics, 
the result would typically be considered undefined or a floating-point NaN (not a number).
However, NumPy's behavior in this case is to suppress the error and return 0.
'''

# Performing floor division on arrays containing zero
print("\nExample 3: Performing floor division on arrays containing zero")
print(np.array(0) // np.array(0))

# Creating a NumPy array containing NaN (not a number)
print("\nExample 4: Creating a NumPy array containing NaN")
print(np.array([np.nan]))

# Converting NaN to an integer
print("\nExample 5: Converting NaN to an integer")
print(np.array([np.nan]).astype(int)) # Note: Converting NaN to an integer results in the minimum integer value

# Converting NaN to a floating-point number
print("\nExample 6: Converting NaN to a floating-point number")
print(np.array([np.nan]).astype(float)) # Note: Converting NaN to a floating-point number results in NaN.
