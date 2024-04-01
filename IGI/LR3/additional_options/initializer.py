import random

def generate_random_integer():
    """
    Generates a random sequence of int numbers.

    Yields:
        int: The generated number.
    """
    while True:
        yield random.randint(1, 100)
        
def generate_random_float():
    
    """
    Generates a random sequence of float numbers.

    Yields:
        float: The generated number.
    """
    while True:
        yield random.uniform(-20, 20)
        
def generate_int_sequence(n=10):
    """
    Generates a sequence of random integers.

    Args:
        n (int, optional): The number of random integers to generate. Default is 10.

    Returns:
        list: List of random integers.
    """
    random_number_generator = generate_random_integer()
    random_number_list = [next(random_number_generator) for _ in range(n)]
    return random_number_list

def generate_float_sequence(n=10):
    """
    Generates a sequence of random float numbers.

    Args:
        n (int, optional): The number of random float numbers to generate. Default is 10.

    Returns:
        list: List of random float numbers.
    """
    random_number_generator = generate_random_float()
    random_number_list = [next(random_number_generator) for _ in range(n)]
    return random_number_list
def input_int_sequence():
    """
    Initializes a sequence of int numbers using user input.

    Returns:
        list: The initialized sequence.
    """
    sequence = []
    print("Enter numbers (enter 'q' to finish):")
    while True:
        number = input()
        if number == "q":
            break
        try:
            number = int(number)
            sequence.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return sequence


def input_float_sequence():
    """
    Initializes a sequence of float numbers using user input.

    Returns:
        list: The initialized sequence.
    """
    sequence = []
    print("Enter numbers (enter 'q' to finish):")
    while True:
        number = input()
        if number == "q":
            break
        try:
            number = float(number)
            sequence.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return sequence