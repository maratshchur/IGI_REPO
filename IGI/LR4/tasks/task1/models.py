from tasks.task1.decorator import catch_wrong_exam_name

class Person:
    def __init__(self, name):
        self.name = name
        
class Abiturient(Person):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument

class Exam:
    """
    Represents an exam for abiturients.

    Attributes:
        abiturients (list): List of abiturients participating in the exam.
        exam_list (list): List of available exams.

    Methods:
        add_abiturient: Adds an abiturient to the exam.
        exam_participants: Retrieves a list of abiturients participating in a specific exam.
        sort_by_name: Sorts the abiturients by their names.
        get_all_abiturients: Retrieves a dictionary of all abiturients and their instruments.
        get_abiturient_info: Retrieves information about a specific abiturient.
    """

    def __init__(self):
        self.abiturients = []
        self.exam_list = ["piano", "guitar", "violin", "drums"]

    @catch_wrong_exam_name
    def add_abiturient(self, abiturient):
        """
        Adds an abiturient to the exam.

        Args:
            abiturient (Abiturient): The abiturient to be added.

        Raises:
            ValueError: If no exam is found for the abiturient's instrument.
        """
        for exam in self.exam_list:
            if abiturient.instrument.lower() == exam:
                self.abiturients.append(abiturient)
                return
        raise ValueError(f"No exam found for instrument '{abiturient.instrument}'.")

    def exam_participants(self, instrument):
        """
        Retrieves a list of abiturients participating in a specific exam.

        Args:
            instrument (str): The instrument for which to retrieve participants.

        Returns:
            list: List of abiturients participating in the specified exam.
        """
        matching_abiturients = []
        for abiturient in self.abiturients:
            if abiturient.instrument == instrument:
                matching_abiturients.append(abiturient)
        return matching_abiturients

    def sort_by_name(self):
        """
        Sorts the abiturients by their names.

        Returns:
            list: List of abiturients sorted by name.
        """
        sorted_abiturients = sorted(self.abiturients, key=lambda x: x.name)
        return sorted_abiturients

    def get_all_abiturients(self):
        """
        Retrieves a dictionary of all abiturients and their instruments.

        Returns:
            dict: Dictionary mapping abiturient names to their instruments.
        """
        abiturient_dict = {}
        for abiturient in self.abiturients:
            abiturient_dict[abiturient.name] = abiturient.instrument
        return abiturient_dict

    def get_abiturient_info(self, abiturient_name):
        """
        Retrieves information about a specific abiturient.

        Args:
            abiturient_name (str): The name of the abiturient.

        Returns:
            list: List of abiturients matching the specified name.
        """
        matching_abiturients = []
        for abiturient in self.abiturients:
            if abiturient.name == abiturient_name:
                matching_abiturients.append(abiturient)
        return matching_abiturients
        

    # def save_to_csv(self, filename):
    #     with open(filename, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(['Last Name', 'Instrument'])
    #         for abiturient in self.abiturients:
    #             writer.writerow([abiturient.name, abiturient.instrument])

    # def save_to_pickle(self, filename):
    #     with open(filename, 'wb') as file:
    #         pickle.dump(self.abiturients, file)

    # def load_from_pickle(self, filename):
    #     with open(filename, 'rb') as file:
    #         self.abiturients = pickle.load(file)