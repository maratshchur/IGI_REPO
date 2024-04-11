import numpy as np

class Matrix(list):
    
    def __init__(self,n ,m):
        self.matrix = np.random.randint(-10, 10, size=(n, m))
        
    def __str__(self):
        return self.matrix.__str__()
    
    def numpy_variance(self):
        return np.var(self.matrix)
    
    def numpy_mean(self):
        return np.mean(self.matrix)
    
    def numpy_std(self):
        return np.std(self.matrix)
    
    def variance(self):
        """
        Calculates the variance of the elements in a matrix.

        Parameters:
        matrix (numpy.ndarray): Input matrix.

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
        abs_matrix = np.abs(self.matrix)  
        max_abs_index = np.unravel_index(np.argmax(abs_matrix), abs_matrix.shape)
        max_abs = self.matrix[max_abs_index]  
        return max_abs
        
    def divide_matrix_on_max_abs_element(self):
        self.matrix = self.matrix / self.find_max_abs()
        
class ModificatedMatrix(Matrix, ABSMixin):
    pass