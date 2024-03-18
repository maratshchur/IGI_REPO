from additional_options.initializer import generate_int_sequence, input_int_sequence
from additional_options.choose_options import choose_initializing_way
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
    if sequence==None:
        print("Incorrect choice")
        return
    find_minimum_sum(sequence)