from tasks.task3.additional_options.validation import validate_x_value, validate_float_value
from tasks.task3.models import LNCalculator
from math import log
import numpy as np
import matplotlib.pyplot as plt
from tasks.task3.data import FUNCTION_PATH

def build_plot():
    """
    Builds and saves a plot of the function ln(1+x).

    The plot is saved as 'function.png' and displayed on the screen.

    Parameters:
        None

    Returns:
        None
    """
    x = np.linspace(-0.9, 1, 100)
    y = np.log(1 + x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('ln(1+x)')
    plt.title('Graph of ln(1+x)')
    plt.grid(True)
    plt.savefig(FUNCTION_PATH)
    plt.show()
    
    
def task3():
    
    calculator = LNCalculator()
    x = input("Enter x: ")
    if not validate_x_value(x):
        print("Invalid value of x")
        return 
    x = validate_float_value(x)
    eps = input("Enter the desired precision (eps): ")
    eps = validate_float_value(eps)
    if eps is None:
        print("Invalid value of eps")
        return
    result, n = calculator.calculate_ln_series(x, eps)
    mean, median, mode, variance, standard_deviation = calculator.calculate_statistics()
    
    print("x        n       F(x)        Math F(x)       eps")
    print(f"{x:.3f}   ", n, f"      {result:.3f}", f"       {log(1+x):.3f}          ", eps)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Mode: ", mode)
    print("Variance: ", variance)
    print("Standard Deviation: ", standard_deviation)
    
    calculator.plot_graphs()
    build_plot()
    