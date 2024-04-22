import numpy as np  # Import the NumPy library and alias it as "np"

print(np.__version__)  # Print the version of NumPy installed

# Print the NumPy build configuration information
# This includes details such as compiler information, BLAS and LAPACK libraries, and CPU architecture
np.show_config()