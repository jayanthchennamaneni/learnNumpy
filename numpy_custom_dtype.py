"""

This script demonstrates the usage of the np.dtype() function in NumPy to define a custom data type.
The custom data type includes fields for red (r), green (g), blue (b), and alpha (a) components, each represented by unsigned 8-bit integers. 

"""

import numpy as np

# Defining a custom data type using np.dtype()
custom_dtype = np.dtype([
    ("r", np.ubyte),
    ("g", np.ubyte),
    ("b", np.ubyte),
    ("a", np.ubyte)
])

print("Custom Data Type:")
print(custom_dtype)


