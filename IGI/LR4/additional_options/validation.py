def validate_int_value(x):
    """
    Validates and converts the input value to an integer.

    Args:
        x (any): The input value.

    Returns:
        int or None: The validated integer value if conversion is successful, None otherwise.
    """
    try:
        x = int(x)
        return x
    except ValueError:
        return None

def validate_float_value(x):
    """
    Validates and converts the input value to an integer.

    Args:
        x (any): The input value.

    Returns:
        int or None: The validated integer value if conversion is successful, None otherwise.
    """
    try:
        x = float(x)
        return x
    except ValueError:
        return None
    
def validate_figure_parameters(side_length, color):
    if side_length <= 0 or side_length==None:
        return False
    if not color:
        return False
    return True

