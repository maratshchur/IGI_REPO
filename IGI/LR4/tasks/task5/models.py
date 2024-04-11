import numpy as np

class Matrix(list):
    
    def __init__(self, n, m):
        """
        Initializes a Matrix object with random integer values.

        Parameters:
        n (int): Number of rows in the matrix.
        m (int): Number of columns in the matrix.
        """
        self.matrix = np.random.randint(-10, 10, size=(n, m))
        
    def __str__(self):
        """
        Returns a string representation of the matrix.

        Returns:
        str: String representation of the matrix.
        """
        return self.matrix.__str__()
    
    def numpy_variance(self):
        """
        Calculates the variance of the elements in the matrix using numpy.

        Returns:
        float: Variance of the elements in the matrix.
        """
        return np.var(self.matrix)
    
    def numpy_mean(self):
        """
        Calculates the mean of the elements in the matrix using numpy.

        Returns:
        float: Mean of the elements in the matrix.
        """
        return np.mean(self.matrix)
    
    def numpy_std(self):
        """
        Calculates the standard deviation of the elements in the matrix using numpy.

        Returns:
        float: Standard deviation of the elements in the matrix.
        """
        return np.std(self.matrix)
    
    def variance(self):
        """
        Calculates the variance of the elements in the matrix.

        Returns:
        float: Variance of the elements in the matrix.
        """
        mean = np.sum(self.matrix) / self.matrix.size

        squared_diff = (self.matrix - mean) ** 2
        sum_squared_diff = np.sum(squared_diff)
        variance = sum_squared_diff / self.matrix.size

        return variance
    

class ABSMixin:
    def find_max_abs(self):
        """
        Finds the maximum absolute value in the matrix.

        Returns:
        int: Maximum absolute value in the matrix.
        """
        abs_matrix = np.abs(self.matrix)
        max_abs_index = np.unravel_index(np.argmax(abs_matrix), abs_matrix.shape)
        max_abs = self.matrix[max_abs_index]
        return max_abs
        
    def divide_matrix_on_max_abs_element(self):
        """
        Divides all elements in the matrix by the maximum absolute value.
        """
        self.matrix = self.matrix / self.find_max_abs()
        
class ModificatedMatrix(Matrix, ABSMixin):
    pass