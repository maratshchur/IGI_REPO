import numpy as np

def generate_random_int():
    """
    Generates a random integer between 1 and 3 (inclusive).

    Returns:
    int: Random integer between 1 and 3.
    """
    return np.random.randint(1, 4)

def generate_matrix(n, m):
    """
    Generates a random matrix of size n x m with integer values ranging from -10 to 10.

    Parameters:
    n (int): Number of rows in the matrix.
    m (int): Number of columns in the matrix.

    Returns:
    numpy.ndarray: Random matrix of size n x m.
    """
    return np.random.randint(-10, 10, size=(n, m))