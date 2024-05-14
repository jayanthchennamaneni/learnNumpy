# Datetime and Timedelta Support

NumPy provides extensive support for working with dates, times, and time intervals through the datetime64 and timedelta64 data types. Here's an overview of datetime and timedelta support in NumPy. This feature is essential for tasks involving time-series data, simulations, and various other applications where handling temporal data is crucial.

## Overview

NumPy's datetime and timedelta support allows for creating arrays of datetime objects and performing arithmetic operations with timedeltas. This enables manipulation and analysis of temporal data, including calculating differences between dates, adding or subtracting time intervals, and working with timezones.

## Key Features

- **Working with Dates and Times**: Learn how to create arrays of datetime objects, parse strings into datetime objects, and perform various operations with dates and times.
- **Timedelta Arithmetic**: Understand how to create timedeltas, perform arithmetic operations with timedeltas, and apply them to datetime arrays for date manipulation.

## Datetime64

The datetime64 data type represents dates and times in NumPy arrays. Key features include:
- Stores dates/times as 64-bit integers with configurable time units (e.g., seconds, milliseconds, days).
- Can be created from strings in ISO 8601 format or Python's datetime objects.
- Supports arithmetic operations like addition/subtraction of timedeltas.

```python
# Use NumPy's datetime functions to create datetime arrays, parse strings into datetime objects, and perform operations with dates and times:

import numpy as np
import datetime

# From string
dt = np.datetime64('2023-05-11T12:30')  

# From datetime object 
dt = np.datetime64(datetime.datetime(2023, 5, 11, 12, 30))

# Create a datetime array
dates = np.array(['2024-05-10', '2024-05-11'], dtype='datetime64')

# Parse strings into datetime objects
date_str = np.array(['2024-05-10', '2024-05-11'], dtype='datetime64')
dates_parsed = np.datetime64(date_str)

# Extract components of datetime objects
print(np.datetime64('2024-05-10', 'D').astype('datetime64[D]'))

```

## Timedelta64

The timedelta64 data type represents time intervals/durations in NumPy arrays. Key features include:
- Stores time intervals as 64-bit integers with configurable units (e.g., seconds, days, weeks).
- Can be created from integer values or strings representing durations.
- Supports arithmetic operations like addition, subtraction, multiplication, and division.

**Timedelta Arithmetic**: 

```python
# Use NumPy's timedelta functions to create timedeltas, perform arithmetic operations with timedeltas, and apply them to datetime arrays:

# Create a datetime array
dates = np.array(['2024-05-10', '2024-05-11'], dtype='datetime64')

# Create a timedelta object
delta = np.timedelta64(1, 'D')

# Add timedelta to datetime array
new_dates = dates + delta
```

## Combination of both 

NumPy supports arithmetic operations between datetime64 and timedelta64 objects, enabling date/time calculations:

```python
# Datetime + Timedelta
dt = np.datetime64('2023-05-11T12:30') 
td = np.timedelta64(2, 'D')
new_date = dt + td  # 2023-05-13T12:30

# Datetime - Datetime = Timedelta  
dt1 = np.datetime64('2023-05-11T12:30')
dt2 = np.datetime64('2023-05-10T08:00') 
duration = dt1 - dt2  # 1 day, 4:30:00
```

## Resources

- NumPy Documentation: [Datetime support](https://numpy.org/doc/stable/reference/arrays.datetime.html)

---