# Lab Assignment: 
# Program Name: Power Series Calculation
# Program Version: 1.0
# Developer: Marat Shchur
# Date: 2024-03-05

import math
from math import log
from additional_options.validation import validate_float_value, validate_x_value
from additional_options.print import print_results
from additional_options.decorator import decorator
MAX_ITERATIONS = 500

def calculate_ln_series(x, eps):
    """
    Calculates the value of ln(1+x) using power series expansion.

    Args:
        x (float): The input value for the ln(x) function.
        eps (float): The desired precision for the calculation.

    Returns:
        tuple: The calculated value of ln(x) and the number of terms required.
    """
    result = 0.0
    term = 0
    n = 0

    while abs(log(1+x) - result) >= eps and n < MAX_ITERATIONS:
        result += term
        term = (-1)**(n) * (x**(n+1)) / (n+1)
        n += 1

    return result, n



@decorator    
def task1():
    x = input()
    if not validate_x_value(x):
        print("Invalid value of x")
        return None, None
    x=validate_float_value(x)
    eps = input("Enter the desired precision (eps): ")
    eps = validate_float_value(eps)
    if eps==None:
        print("Invalid value of eps")
        return None, None
    result, n = calculate_ln_series(x, eps)
    return result, n
