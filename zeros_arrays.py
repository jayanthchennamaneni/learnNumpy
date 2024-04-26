import numpy as np  # Importing NumPy library and aliasing it as np

# Creating a 1D array of zeros with 10 elements
a = np.zeros(10)
print(a) 
print(f"{a.size * a.itemsize} bytes")  # Printing the memory size of the array in bytes

# Creating a 2D array of zeros with shape (10, 10)
b = np.zeros((10,10))
print(b)
print(f"{b.size * b.itemsize} bytes")  # Printing the memory size of the array in bytes

# Creating a 3D array of zeros with shape (2, 10, 10)
c = np.zeros((2,10,10))
print(c)
print(f"{c.size * c.itemsize} bytes")  # Printing the memory size of the array in bytes
