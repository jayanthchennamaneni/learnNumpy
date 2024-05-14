# Linear Algebra in NumPy

## Overview

NumPy's linear algebra capabilities are built on top of optimized BLAS (Basic Linear Algebra Subprograms) and LAPACK (Linear Algebra PACKage) libraries, ensuring efficient and reliable computations. These functions are widely used in scientific computing, machine learning, physics, engineering, computer graphics and various other domains that involve linear algebra operations.

NumPy provides comprehensive support for linear algebra operations, making it a powerful tool for solving mathematical problems involving vectors, matrices, and higher-dimensional arrays. Here are some key linear algebra capabilities in NumPy:

## Basic Linear Algebra Operations

NumPy provides a rich set of functions for performing basic linear algebra operations, including:
- Vector addition and subtraction
- Scalar-vector and scalar-matrix multiplication
- Matrix multiplication (dot product)
- Transpose of a matrix
- Matrix determinant and inverse


## Matrix and Vector Products

In NumPy, vectors are represented as one-dimensional arrays, while matrices are represented as two-dimensional arrays. Understanding the properties and operations associated with vectors and matrices is crucial for performing linear algebra computations efficiently.

- `np.dot(a, b)`: Computes the dot product of two arrays `a` and `b`. For 2D arrays, it performs matrix multiplication.
- `np.inner(a, b)`: Computes the inner product of vectors for 1D arrays, and matrix multiplication for 2D arrays.
- `np.outer(a, b)`: Computes the outer product of two vectors.
- `np.matmul(a, b)`: Computes the matrix product of two arrays. This is the preferred function for matrix multiplication.

```python

"""
## Matrix Multiplication

Matrix multiplication in NumPy is performed using the `np.dot()` function or the `@` operator. It supports various types of matrix multiplication, including:
- Element-wise multiplication (Hadamard product) using the `*` operator.
- Dot product of two arrays using `np.dot()` or the `@` operator.
- Batch matrix multiplication for higher-dimensional arrays.
"""

import numpy as np

# Define two arrays for matrix and vector products
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Compute dot product of arrays a and b
dot_product = np.dot(a, b)
print(dot_product)

# Compute inner product of arrays a and b
inner_product = np.inner(a, b)
print(inner_product)

# Compute outer product of arrays a and b
outer_product = np.outer(a, b)
print(outer_product)

# Compute matrix product of arrays a and b
matrix_product = np.matmul(a, b)
print(matrix_product)
```

## Matrix Decompositions and Norms

- `np.linalg.cholesky(a)`: Computes the Cholesky decomposition of a matrix.
- `np.linalg.qr(a)`: Computes the QR decomposition of a matrix.
- `np.linalg.svd(a)`: Computes the Singular Value Decomposition (SVD) of a matrix.
- `np.linalg.norm(a)`: Computes the matrix or vector norm.

```python
import numpy as np

# Define a matrix for decomposition and norm computations
a = np.array([[1, 2], [3, 4]])

# Compute Cholesky decomposition of matrix a
cholesky_decomposition = np.linalg.cholesky(a)
print(cholesky_decomposition)

# Compute QR decomposition of matrix a
qr_decomposition = np.linalg.qr(a)
print(qr_decomposition)

'''
Singular value decomposition is a factorization method that decomposes a matrix into the product of three matrices. SVD has various applications, including image compression, data analysis, and dimensionality reduction. NumPy provides the function `numpy.linalg.svd()` for computing the SVD of a matrix.
'''
# Compute SVD of matrix a
svd_result = np.linalg.svd(a)
print(svd_result)

# Compute matrix norm of matrix a
matrix_norm = np.linalg.norm(a)
print(matrix_norm)
```
## Linear Systems
- One of the most common applications of linear algebra is solving systems of linear equations. NumPy provides functions like `numpy.linalg.solve()` for solving systems of linear equations represented in matrix form.

- `np.linalg.solve(a, b)`: Solves the linear matrix equation `ax = b` for `x`.
- `np.linalg.lstsq(a, b)`: Computes the least-squares solution to `ax = b`.
- `np.linalg.inv(a)`: Computes the multiplicative inverse of a square matrix `a`.

```python
import numpy as np

# Define arrays for linear system solving
a = np.array([[2, 3], [4, 5]])
b = np.array([5, 6])

# Solve linear system ax = b for x
solution = np.linalg.solve(a, b)
print(solution)

# Compute least-squares solution to ax = b
lstsq_solution = np.linalg.lstsq(a, b)
print(lstsq_solution)

'''
NumPy offers functions for computing the inverse of a matrix, such as `np.linalg.inv()` for ordinary matrices and `np.linalg.pinv()` for pseudo-inverses of singular matrices.
'''

# Compute multiplicative inverse of matrix a
inverse_matrix = np.linalg.inv(a)
print(inverse_matrix)
```

## More Linear Algebra Functions

- `np.linalg.det(a)`: Computes the determinant of a square matrix `a`.
- `np.linalg.eig(a)`: Computes the eigenvalues and right eigenvectors of a square matrix `a`.
- `np.linalg.matrix_rank(a)`: Computes the matrix rank of `a`.
- `np.trace(a)`: Computes the sum of the diagonal elements of `a`.

```python
import numpy as np

# Define a matrix for other linear algebra functions
a = np.array([[1, 2], [3, 4]])

# Compute determinant of matrix a
determinant = np.linalg.det(a)
print(determinant)

'''
Eigenvalues represent the scaling factors of the eigenvectors in a linear transformation. NumPy's `np.linalg.eigvals()` function computes the eigenvalues of a square matrix.

Eigenvectors are vectors that remain in the same direction after a linear transformation. NumPy's `np.linalg.eig()` function computes both the eigenvalues and eigenvectors of a square matrix.

Application of Eigenvalues and Eigenvectors: 

Eigenvalues and eigenvectors have various applications in linear algebra, such as:
- Determining stability in dynamic systems.
- Principal component analysis (PCA) for dimensionality reduction.
- Solving differential equations in physics and engineering.
'''

# Compute eigenvalues and eigenvectors of matrix a
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)

# Compute matrix rank of matrix a
matrix_rank = np.linalg.matrix_rank(a)
print(matrix_rank)

# Compute trace of matrix a
trace = np.trace(a)
print(trace)
```

## Additional Resources

- [NumPy Linear Algebra Documentation](https://numpy.org/doc/stable/reference/routines.linalg.html): NumPy documentation on linear algebra routines.

---




