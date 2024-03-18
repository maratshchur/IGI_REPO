from additional_options.initializer import generate_int_sequence, input_int_sequence
from data import TASK_TUTORIAL
def choose_task_number():
    """
    Prompts the user to choose a task number.
    
    Returns:
        str: The selected task number.
    """
    task_number = input(TASK_TUTORIAL)
    return task_number


def continue_program_request():
    """
    Prompts the user if they want to continue with the calculation.
    
    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    repeat = input("Do you want to calculate again? (yes/no): ")
    if repeat.lower() == "yes":
        return True
    else:
        return False
    
def choose_initializing_way(func1, func2):
    """
    Allows the user to choose a way to initialize a sequence.
    
    Args:
        func1 (callable): A function to generate a sequence.
        func2 (callable): A function to input a sequence.
    
    Returns:
        sequence: The initialized sequence.
    """
    choice = input("Choose an option:\n1. Generate a sequence\n2. Input a sequence\n")
    if choice == "1":
        sequence = func1()  # Generate a sequence
    elif choice == "2":
        sequence = func2()  # Input a sequence
    else:
        return
    return sequence

