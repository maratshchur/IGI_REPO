from tasks.task5.initializer import generate_random_int, generate_matrix
import numpy as np


def matrix_variance(matrix):
    """
    Calculates the variance of the elements in a matrix.

    Parameters:
    matrix (numpy.ndarray): Input matrix.

    Returns:
    float: Variance of the elements in the matrix.
    """
    mean = np.sum(matrix) / matrix.size

    squared_diff = (matrix - mean) ** 2
    sum_squared_diff = np.sum(squared_diff)
    variance = sum_squared_diff / matrix.size

    return variance

def task5():
    n = generate_random_int()
    m = generate_random_int()
    matrix_1 = generate_matrix(n, m)
    
    print("Original matrix:")
    print(matrix_1)

    
    abs_matrix = np.abs(matrix_1)  
    max_abs_index = np.unravel_index(np.argmax(abs_matrix), abs_matrix.shape)
    max_abs = matrix_1[max_abs_index]  
    print("Max element: ", max_abs)

    matrix_2 = matrix_1 / max_abs
    
    print("New matrix: ")
    print(matrix_2)
    
    variance_1 = np.var(matrix_2)
    variance_2 = matrix_variance(matrix_2)
    print("Variance of matrix (standart function): {:.2f}".format(variance_1))
    print("Variance of matrix (my function): {:.2f}".format(variance_2))
    
    mean_value = np.mean(matrix_2)
    print("Mean value:", mean_value)

    # median_value = np.median(matrix_2)
    # print("Median:", median_value)

    # corr_matrix = np.corrcoef(matrix_2)
    # print("Correlation matrix:")
    # print(corr_matrix)

    std_value = np.std(matrix_2)
    print("Standard deviation:", std_value)