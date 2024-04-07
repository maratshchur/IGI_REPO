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