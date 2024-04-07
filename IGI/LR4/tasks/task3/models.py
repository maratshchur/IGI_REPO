import math
import matplotlib.pyplot as plt
from math import log




class LNCalculator:
    MAX_ITERATIONS = 500
    def __init__(self):
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
        mean = self.result / self.iterations
        median = sorted(self.values)[len(self.values) // 2]
        mode = max(set(self.values), key=self.values.count)

        variance = sum((x - mean) ** 2 for x in self.values) / len(self.values)
        standard_deviation = math.sqrt(variance)

        return mean, median, mode, variance, standard_deviation

    def plot_graphs(self):
        sum = 0
        function_values = []
        for term in self.values:
            function_values.append(sum)
            sum+=term
        iteration_values = [i+1 for i in range(self.iterations)]
        plt.plot(iteration_values, function_values)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Iterations')
        plt.ylabel('Function value')
        plt.title('Value of ln(1+x) using power series expansion')
        plt.annotate("End of power series expansion", xy=(self.iterations,self.result),xytext=(4,0.3),arrowprops=dict(facecolor="black",shrink=0.05))
        plt.grid(True)
        plt.savefig('series.png')
        plt.show()
        