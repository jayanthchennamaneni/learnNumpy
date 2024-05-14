# File Handling: File Input and Output operations with NumPy

## Overview

File Input and Output (I/O) operations are essential for working with data in NumPy. NumPy provides several functions for file handling, allowing you to save and load NumPy arrays to and from various file formats. Here's an overview of file input and output operations in NumPy:

## Loading NumPy Arrays

NumPy provides functions to read data from files into arrays:

- `np.load()`: Load a single NumPy array or pickled object from a binary NPY file.
- `numpy.loadtxt()`: Loads data from a text file.
- `numpy.genfromtxt()`: Loads data from a text file, handling missing values gracefully.
- `numpy.fromfile()`: Reads binary data from a file into an array.
- `np.fromregex()`: Construct a NumPy array from a text file using regular expressions.

The `np.loadtxt` and `np.genfromtxt` functions provide various options for handling text files, such as specifying data types, delimiters, comment characters, skipping rows, and selecting specific columns.

```python
# Example for loading data:
import numpy as np

# Load data from a text file
data = np.loadtxt('data.txt')

# Load data from a CSV file with missing values
data = np.genfromtxt('data.csv', delimiter=',')

# Read binary data into an array
data = np.fromfile('data.bin', dtype=np.float32)
```

## Saving Data with NumPy

You can also save NumPy arrays to various file formats:

### To Binary Files (NPY, NPZ)

- `numpy.save()`: Saves a single array to a binary file in NumPy `.npy` format.
- `numpy.savez()`: Saves multiple arrays into a single NumPy file in in an uncompressed `.npz` format.
- `numpy.savez_compressed()`: Saves multiple arrays into a compressed `.npz` file.

### To Text Files
- `numpy.savetxt()`: Saves an array to a text file.
- `np.fromstring()`: Construct a NumPy array from text data in a string.

```python
# Example for saving data
import numpy as np

# Save array to a text file
np.savetxt('data.txt', data)

# Save a single array to a binary file
np.save('data.npy', data)

# Save multiple arrays to a compressed file
np.savez_compressed('data.npz', array1=data1, array2=data2)
```

## Memory-Mapped Files

- `np.memmap()`: Create a memory-mapped NumPy array from a binary file on disk.

Memory-mapping allows you to work with large arrays without loading the entire array into memory, enabling efficient data processing.

## Supported File Formats

NumPy's file handling capabilities allow you to seamlessly save and load NumPy arrays to and from various file formats, facilitating data storage, sharing, and analysis workflows in scientific computing and data analysis applications. NumPy supports various file formats for both reading and writing data, including:

- Text files (CSV, TXT)
- Binary files (`.npy`, `.npz`)
- Comma-separated values (CSV)
- Delimited text files
- Custom binary formats

## Resources

For more information on file input and output with NumPy, refer to the [NumPy documentation](https://numpy.org/doc/stable/reference/routines.io.html).

---






