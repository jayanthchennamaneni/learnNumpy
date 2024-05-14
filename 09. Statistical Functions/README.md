# Statistical Functions and Descriptive Statistics

Statistical functions and descriptive statistics in NumPy provide tools for analyzing and summarizing data. These functions allow users to compute various statistical metrics, perform descriptive analysis, and aggregate data efficiently within NumPy arrays.

## Overview

NumPy offers a wide range of statistical functions to analyze data arrays, compute descriptive statistics, and perform aggregation and reduction operations. These functions are essential for understanding the distribution and characteristics of data, making them a fundamental component of data analysis and scientific computing workflows.

## Key Features

- **Descriptive Statistics**: Explore functions for computing basic statistical metrics such as mean, median, variance, standard deviation, and percentiles.
- **Statistical Functions**: Learn about functions for calculating various statistical measures including correlation, covariance, skewness, and kurtosis.
- **Aggregation and Reduction Operations**: Understand how to aggregate and reduce data along specified axes using functions like sum, mean, max, min, and more.


## Descriptive Statistics

Use NumPy's functions to compute descriptive statistics for your data arrays:

    - **np.mean():** Computes the arithmetic mean along the specified axis.
    - **np.median():** Computes the median along the specified axis.
    - **np.std():** Computes the standard deviation along the specified axis.
    - **np.var():** Computes the variance along the specified axis.
    - **np.percentile():** Computes the q-th percentile of the data along the specified axis.
    - **np.quantile():** Computes the q-th quantile of the data along the specified axis.
    - **np.amin():** Computes the minimum value along the specified axis.
    - **np.amax():** Computes the maximum value along the specified axis.
    - **np.ptp():** Computes the range (maximum - minimum) along the specified axis.

```python
# Compute mean, median, and mode
data = np.array([1, 2, 3, 4, 5])
print(np.mean(data))
print(np.median(data))
```

## Statistical Functions

Utilize NumPy's functions to perform various statistical calculations:

    - **np.corrcoef():** Computes the correlation coefficient between two arrays.
    - **np.cov():** Computes the covariance matrix between arrays.

```python
# Compute correlation and covariance
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([5, 4, 3, 2, 1])
print(np.corrcoef(data1, data2))
print(np.cov(data1, data2))
```

## Aggregation and Reduction Operations

Apply aggregation and reduction operations to your data arrays:

    - **np.average():** Computes the weighted average along the specified axis, with optional weights.
    - **np.mean():** Computes the arithmetic mean, which is the same as np.average() without weights.

```python
# Sum and average data
data = np.array([[1, 2], [3, 4], [5, 6]])
print(np.sum(data, axis=0))
print(np.mean(data, axis=1))
```

## Resources

- NumPy Documentation: [Statistical functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

---

