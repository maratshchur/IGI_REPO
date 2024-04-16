import math
import matplotlib.pyplot as plt
from math import log
from tasks.task3.data import PICTURE_PATH, MYFUNCTION_PATH
import numpy as np


class LNCalculator:
    MAX_ITERATIONS = 500

    def __init__(self):
        """
        Initialize the LNCalculator object.
        """
        self.result = 0
        self.iterations = 0
        self.values = []

    def calculate_ln_series(self, x, eps):
        """
        Calculates the value of ln(1+x) using power series expansion.

        Args:
            x (float): The input value for the ln(x) function.
            eps (float): The desired precision for the calculation.

        Returns:
            tuple: The calculated value of ln(x) and the number of terms required.
        """
        self.eps = eps
        self.result = 0.0
        term = 0
        self.iterations = 0
        self.values = []

        while abs(log(1+x) - self.result) >= eps and self.iterations < self.MAX_ITERATIONS:
            self.result += term
            self.values.append(term)
            term = (-1)**(self.iterations) * (x**(self.iterations+1)) / (self.iterations+1)
            self.iterations += 1
        return self.result, self.iterations

    def calculate_statistics(self):
        """
        Calculates statistics of the calculated values.

        Returns:
            tuple: The calculated mean, median, mode, variance, and standard deviation.
        """
        mean = self.result / self.iterations
        median = sorted(self.values)[len(self.values) // 2]
        mode = max(set(self.values), key=self.values.count)

        variance = sum((x - mean) ** 2 for x in self.values) / len(self.values)
        standard_deviation = math.sqrt(variance)

        return mean, median, mode, variance, standard_deviation

class PlotMixin:
    def plot_graphs(self):
        """
        Plots the graph of the function values during the power series expansion.

        Saves the graph as 'series.png' and displays it.
        """
        sum = 0
        function_values = []
        for term in self.values:
            function_values.append(sum)
            sum += term
        iteration_values = [i+1 for i in range(self.iterations)]
        plt.plot(iteration_values, function_values)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Iterations')
        plt.ylabel('Function value')
        plt.title('Value of ln(1+x) using power series expansion')
        plt.annotate("End of power series expansion", xy=(self.iterations, self.result), xytext=(4, 0.3),
                     arrowprops=dict(facecolor="black", shrink=0.05))
        plt.grid(True)
        plt.savefig(PICTURE_PATH)
        plt.show()
        
    def function_plot(self):
        x_data = np.linspace(-0.9, 0.9, 100)
        y_data = []
        for x in x_data:
            a, b = self.calculate_ln_series(x,self.eps)
            y_data.append(a)
        y_data=np.array(y_data)
        
        plt.plot(x_data, y_data, color='blue', label='My series expansion Function')
        
        x_data = np.linspace(-0.9, 0.9, 100)
        y_data = np.log(1 + x_data)
        
        plt.plot(x_data, y_data, color='red', label='Original Function')
        
        plt.xlabel('x')
        plt.ylabel('ln(1+x)')
        plt.title('Graph of ln(1+x)')
        plt.grid(True)
        plt.savefig(MYFUNCTION_PATH)
        plt.show()

class LNDrawing(LNCalculator, PlotMixin):
    pass