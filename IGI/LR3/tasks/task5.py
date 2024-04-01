from additional_options.initializer import generate_float_sequence, input_float_sequence
from additional_options.choose_options import choose_initializing_way
from additional_options.print import print_list
from additional_options.validation import validate_list

def find_max_abs_value(elements):
    """
    Find the maximum absolute value in the list.

    Args:
        elements (list): The list of elements.

    Returns:
        float: The maximum absolute value in the list.
    """
    max_abs_value = max(elements, key=abs)
    return abs(max_abs_value)


def sum_before_last_positive(elements):
    """
    Calculate the sum of the elements in the list before the last positive element.

    Args:
        elements (list): The list of elements.

    Returns:
        float: The sum of the elements in the list before the last positive element.
    """
    last_positive_index = -1
    for i, element in enumerate(elements):
        if element > 0:
            last_positive_index = i
    sum_before_last_positive = sum(elements[:last_positive_index])
    return sum_before_last_positive


def task5():
    """
    The main function to execute the program.

    Returns:
        None
    """
    elements = choose_initializing_way(generate_float_sequence, input_float_sequence)
    if elements==None:
        print("Incorrect choice")
        return
    if validate_list(elements):
        print_list(elements)
        max_abs_value = find_max_abs_value(elements)
        sum_before_positive = sum_before_last_positive(elements)
        print("Maximum absolute value in the list:", max_abs_value)
        print("Sum of the elements in the list before the last positive element:", sum_before_positive)
    else:
        print("The list is empty.")
