# Numerical Differentiation and Integration

Numerical differentiation and integration are fundamental techniques in numerical analysis, crucial for solving various problems in science and engineering.

## Numerical Differentiation Methods

Numerical differentiation involves approximating the derivative of a function using discrete data points. One common method is the Finite Differences method.

### Finite Differences

The Finite Differences method approximates derivatives by using differences between function values at discrete points.

```python
import numpy as np

# Define a function
def f(x):
    return np.sin(x)

# Points at which to approximate the derivative
x = np.linspace(0, 2*np.pi, 100)
dx = x[1] - x[0]  # Assuming uniform spacing

# First-order forward difference
def forward_difference(f, x, dx):
    return (f(x + dx) - f(x)) / dx

# First-order backward difference
def backward_difference(f, x, dx):
    return (f(x) - f(x - dx)) / dx

# Central difference
def central_difference(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

# Compute derivatives
forward_diff = forward_difference(f, x, dx)
backward_diff = backward_difference(f, x, dx)
central_diff = central_difference(f, x, dx)

# Plotting
import matplotlib.pyplot as plt

plt.plot(x, np.cos(x), label='Analytical Derivative')
plt.plot(x, forward_diff, label='Forward Difference')
plt.plot(x, backward_diff, label='Backward Difference')
plt.plot(x, central_diff, label='Central Difference')
plt.legend()
plt.show()
```

## Numerical Integration Techniques

Numerical integration involves approximating the integral of a function using discrete data points. Quadrature is a common technique for numerical integration.

#### Quadrature

Quadrature methods approximate the definite integral of a function, often using weighted sums of function values at specified points within the integration domain.

```python
from scipy.integrate import quad

# Define a function to integrate
def f(x):
    return np.sin(x)

# Compute the definite integral
integral, error = quad(f, 0, 2*np.pi)

print(f"Integral of sin(x) from 0 to 2*pi: {integral} (with error estimate: {error})")
```

### Practical Example: Trapezoidal and Simpson's Rule

Two common numerical integration methods are the Trapezoidal Rule and Simpson's Rule.

#### Trapezoidal Rule

The Trapezoidal Rule approximates the integral by summing the areas of trapezoids formed under the curve.

```python
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return (dx / 2) * np.sum(y[:-1] + y[1:])

# Example usage
a, b = 0, 2*np.pi
n = 100
integral_trap = trapezoidal_rule(f, a, b, n)

print(f"Trapezoidal Rule Integral: {integral_trap}")
```

#### Simpson's Rule

Simpson's Rule approximates the integral by fitting parabolas to segments of the function.

```python
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be an even integer.")
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return (dx / 3) * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

# Example usage
n = 100  # Must be even
integral_simp = simpsons_rule(f, a, b, n)

print(f"Simpson's Rule Integral: {integral_simp}")
```

---