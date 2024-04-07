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
