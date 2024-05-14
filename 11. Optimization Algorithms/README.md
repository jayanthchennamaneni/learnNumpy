
# Optimization and Root Finding

Optimization and root finding are critical techniques in numerical computing, essential for various scientific, engineering, and data analysis applications.

## Optimization Algorithms (e.g., Gradient Descent)

Optimization involves finding the minimum or maximum of a function. Gradient Descent is a popular optimization algorithm used to minimize functions by iteratively moving towards the steepest descent direction.

### Gradient Descent

Gradient Descent aims to minimize a function by iteratively updating the parameters in the opposite direction of the gradient of the function.

```python
import numpy as np

def gradient_descent(f, grad_f, initial_guess, learning_rate=0.01, max_iters=1000, tol=1e-6):
    x = initial_guess
    for i in range(max_iters):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    return x

# Example function and its gradient
def f(x):
    return x**2 + 4*x + 4

def grad_f(x):
    return 2*x + 4

# Running Gradient Descent
initial_guess = 10.0
min_x = gradient_descent(f, grad_f, initial_guess)
print(f"Minimum value of x: {min_x}")
```

### Root Finding Algorithms (e.g., Newton-Raphson)

Root finding involves solving equations of the form \( f(x) = 0 \). The Newton-Raphson method is a root-finding algorithm that uses derivatives to iteratively find the roots of a real-valued function.

#### Newton-Raphson Method

The Newton-Raphson method uses the formula:

\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

to find successively better approximations to the roots.

```python
def newton_raphson(f, df, initial_guess, max_iters=1000, tol=1e-6):
    x = initial_guess
    for i in range(max_iters):
        f_x = f(x)
        df_x = df(x)
        if df_x == 0:
            raise ValueError("Derivative is zero; no solution found.")
        x_new = x - f_x / df_x
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x

# Example function and its derivative
def f(x):
    return x**2 - 4

def df(x):
    return 2*x

# Running Newton-Raphson Method
initial_guess = 10.0
root_x = newton_raphson(f, df, initial_guess)
print(f"Root of the function: {root_x}")
```

### Practical Example: Logistic Regression

Optimization algorithms like Gradient Descent are commonly used in machine learning for training models. Here's a simplified example of using Gradient Descent for Logistic Regression.

```python
from scipy.special import expit as sigmoid

def logistic_regression(X, y, learning_rate=0.01, max_iters=1000, tol=1e-6):
    m, n = X.shape
    theta = np.zeros(n)
    
    for i in range(max_iters):
        predictions = sigmoid(np.dot(X, theta))
        errors = y - predictions
        gradient = np.dot(X.T, errors) / m
        theta_new = theta + learning_rate * gradient
        
        if np.linalg.norm(theta_new - theta) < tol:
            break
        theta = theta_new
    
    return theta

# Example usage
X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])  # Including bias term
y = np.array([0, 0, 1, 1])

# Train Logistic Regression Model
theta = logistic_regression(X, y)
print(f"Model parameters: {theta}")
```


## Curve Fitting Techniques

Curve fitting is the process of constructing a curve that best fits a series of data points. This is essential in data analysis, scientific research, and engineering to understand underlying trends and make predictions.

### Interpolation and Curve Fitting

Interpolation is a type of curve fitting where you construct new data points within the range of a discrete set of known data points. Curve fitting, on the other hand, can involve finding a function that best fits all the data points, including those outside the known range.

### Interpolation Methods

#### Linear Interpolation

Linear interpolation is the simplest form of interpolation. It assumes that the change between two values is linear and constructs a straight line between two known points.

```python
import numpy as np
import matplotlib.pyplot as plt

# Known data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Points to interpolate
x_new = np.linspace(0, 4, 50)
y_new = np.interp(x_new, x, y)

# Plotting
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Linear Interpolation')
plt.legend()
plt.show()
```

#### Spline Interpolation

Spline interpolation uses piecewise polynomials to interpolate data points, providing a smoother curve compared to linear interpolation.

```python
from scipy.interpolate import interp1d

# Spline interpolation
spline_interpolator = interp1d(x, y, kind='cubic')
y_spline = spline_interpolator(x_new)

# Plotting
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_spline, '-', label='Spline Interpolation')
plt.legend()
plt.show()
```

### Curve Fitting Algorithms

#### Least Squares

The least squares method minimizes the sum of the squares of the residuals (the differences between the observed and calculated values) to find the best-fitting curve.

```python
from scipy.optimize import curve_fit

# Define the model function
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the data
params, covariance = curve_fit(model, x, y)

# Generate fitted data
y_fit = model(x_new, *params)

# Plotting
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_fit, '-', label='Least Squares Fit')
plt.legend()
plt.show()

print(f"Fitted parameters: {params}")
```

### Practical Example: Polynomial Fitting

Polynomial fitting is a common application of least squares fitting, where the data is approximated by a polynomial.

```python
# Polynomial fitting
degree = 2
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

# Generate fitted data
y_polyfit = polynomial(x_new)

# Plotting
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_polyfit, '-', label=f'Polynomial Fit (degree {degree})')
plt.legend()
plt.show()

print(f"Polynomial coefficients: {coefficients}")
```
---