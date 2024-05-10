# NumPy Arrays and Basic Operations

NumPy arrays are the core data structure in NumPy, providing efficient storage and manipulation of data. They are homogeneous collections of elements, all of the same type, indexed by a tuple of non-negative integers. Understanding NumPy arrays and basic operations is fundamental for working effectively with NumPy.

## Creating NumPy Arrays

NumPy arrays are the primary data structure used for numerical computations in NumPy. You can create arrays using various methods, such as:

- Converting lists or tuples to arrays using `numpy.array()`
- enerating arrays with pre-defined shapes and values using functions like `np.zeros()`, `np.ones()`, or `np.arange()`.
- Generating arrays of random numbers using `numpy.random.rand()` or `numpy.random.randn()`
- Loading data from external sources such as CSV files using `np.loadtxt()` or `np.genfromtxt()`.

```python
# Here's an example of creating a NumPy array:

import numpy as np

# Create a 1D array from a list
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr)

# Create a 2D array of zeros
zeros_arr = np.zeros((3, 3))
print("2D Array of Zeros:")
print(zeros_arr)

# Create a 3D array of random numbers
rand_arr = np.random.rand(2, 3, 4)
print("3D Array of Random Numbers:")
print(rand_arr)
```

## Basic Operations with NumPy Arrays

Once NumPy arrays are defined, NumPy enables us to perform various basic operations on them, including:

- Element-wise arithmetic operations (addition, subtraction, multiplication, division) between arrays or between arrays and scalars.
- Array broadcasting: performing operations on arrays with different shapes
- Universal functions (ufuncs) for mathematical operations such as `np.sin()`, `np.cos()`, `np.exp()`, etc.
- Aggregation functions like `np.sum()`, `np.mean()`, `np.min()`, `np.max()` to compute statistics across the array.

```python
# Here's an example of performing basic operations with NumPy arrays:

import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Element-wise addition
result_addition = arr1 + arr2
print(result_addition)

# Element-wise multiplication
result_multiplication = arr1 * arr2
print(result_multiplication)

# Broadcasting example: Adding a scalar to an array
scalar = 10
result_broadcasting = arr1 + scalar
print(result_broadcasting)

# Universal functions (ufuncs): Square root of elements
result_sqrt = np.sqrt(arr1)
print(result_sqrt)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
c = a * b  # Output: [[ 5, 12], [21, 32]]

# Matrix multiplication
d = np.dot(a, b)  # Output: [[19, 22], [43, 50]]
```

## Implicit Type Conversion

NumPy performs implicit type conversion (coercion) during arithmetic operations between arrays of different data types. The data type of the output array is determined based on the data types of the input arrays and the type promotion rules.

### **Type Promotion Rules:**

- If the input arrays have different data types, NumPy promotes the data types to a common data type according to a predetermined hierarchy.
- Data types are promoted from lower to higher precision, with integer types being promoted to floating-point types if necessary.

```python
# Example: element-wise addition between arrays of different data types
import numpy as np

arr_int = np.array([1, 2, 3])         # Create an array of integers
arr_float = np.array([1.5, 2.5, 3.5]) # Create an array of floats

result = arr_int + arr_float         
print(result)                         # Output: [2.5 4.5 6.5]
```

## Additional Resources

- [NumPy Array Creation](https://numpy.org/doc/stable/reference/routines.array-creation.html): NumPy documentation on array creation routines.

---