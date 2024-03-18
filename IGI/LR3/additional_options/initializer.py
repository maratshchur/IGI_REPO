import random

def generate_int_sequence():
    """
    Generates a random sequence of int numbers.

    Returns:
        list: The generated sequence.
    """
    sequence = []
    num_numbers = random.randint(5,10)  # Generates a random number of elements from 5 to 10
    for _ in range(num_numbers):
        number = random.uniform(1, 100)  
        sequence.append(number)
    return sequence


def generate_float_sequence():
    """
    Generates a random sequence of float numbers.

    Returns:
        list: The generated sequence.
    """
    sequence = []
    num_numbers = random.randint(5, 10)  # Generates a random number of elements from 5 to 10
    for _ in range(num_numbers):
        number = random.uniform(-20, 20)  
        sequence.append(number)
    return sequence

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