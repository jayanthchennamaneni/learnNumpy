'''
Numpy is all about vectorization. new friends (among others) are named "vectors", "arrays", "views" or "ufuncs".
'''

import numpy as np
import random
import timeit
from tools import timeit
from itertools import accumulate
np.random.seed(32)

import numpy as np
import random
from itertools import accumulate

# Set seed for reproducibility
np.random.seed(32)

# Object oriented approach
class RandomWalker:
    """
    A class to simulate a random walker.

    Attributes:
        position (int): Current position of the walker.
    """

    def __init__(self):
        self.position = 0  

    def walk(self, n):
        """
        Simulate a random walk of 'n' steps.

        Args:
            n (int): Number of steps to take.

        Yields:
            int: Position of the walker after each step.
        """
        self.position = 0 
        for _ in range(n):
            yield self.position
            self.position += 2 * random.randint(0, 1) - 1

# Procedural Approach
def random_walk(n):
    """
    Simulate a random walk of 'n' steps using a procedural approach.

    Args:
        n (int): Number of steps to take.

    Returns:
        list: List of positions after each step.
    """
    position = 0
    walk = [position]
    for _ in range(n):
        position += 2 * random.randint(0, 1) - 1
        walk.append(position)
    return walk

# Vectorized approach
def random_walk_faster(n):
    """
    Simulate a random walk of 'n' steps using a vectorized approach.

    Args:
        n (int): Number of steps to take.

    Returns:
        list: List of positions after each step.
    """
    # Generate random steps (-1 or +1) using random.choices
    steps = random.choices([-1, +1], k=n)
    # Calculate cumulative sum of steps
    return [0] + list(accumulate(steps))

# Numpy Vectorized approach
def random_walk_fastest(n):
    """
    Simulate a random walk of 'n' steps using a NumPy vectorized approach.

    Args:
        n (int): Number of steps to take.

    Returns:
        numpy.ndarray: Array of positions after each step.
    """
    # Generate random steps (-1 or +1) using np.random.choice
    steps = np.random.choice([-1, +1], n)
    # Calculate cumulative sum of steps using np.cumsum
    return np.cumsum(steps)

walker = RandomWalker()
timeit("[position for position in walker.walk(n=10000)]", globals())

timeit("random_walk(10000)", globals())

timeit("random_walk_faster(10000)", globals())

timeit("random_walk_fastest(10000)", globals())