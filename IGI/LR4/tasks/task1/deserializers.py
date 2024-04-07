import pickle

def load_from_pickle(filename):
    """
    Load data from a pickle file.

    Args:
        filename (str): The name of the pickle file to load data from.

    Returns:
        The data loaded from the pickle file.
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)