from additional_options.initializer import generate_int_sequence, input_int_sequence
from additional_options.choose_options import choose_initializing_way
from additional_options.validation import validate_list

def find_minimum_sum(sequence):
    """
    Finds the minimum value in a sequence based on user input or generated sequence.

    Returns:
        None
    """
    
    minimum = min(sequence)
    print(f"Members of sequence: {sequence}")
    print(f"Minimum value: {minimum}")


def task2():

    sequence = choose_initializing_way(generate_int_sequence, input_int_sequence)
    if not validate_list(sequence):
        print("The list is empty.")
        return
    find_minimum_sum(sequence)