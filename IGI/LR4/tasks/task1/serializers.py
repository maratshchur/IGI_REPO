import csv
import pickle

def save_to_pickle(filename, data: dict):
    """
    Save data to a pickle file.

    Args:
        filename (str): The name of the pickle file to save the data to.
        data (dict): The data to be saved.

    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def save_to_csv(filename, data: dict):
    """
    Save data to a CSV file.

    Args:
        filename (str): The name of the CSV file to save the data to.
        data (dict): The data to be saved.

    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Last Name', 'Instrument'])
        for name, instrument in data.items():
            writer.writerow([name, instrument])