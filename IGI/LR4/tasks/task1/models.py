from tasks.task1.decorator import catch_wrong_exam_name

class Person:
    def __init__(self, name):
        self.name = name
        
class Abiturient(Person):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument

class Exam:
     
    def __init__(self):
        self.abiturients = []
        self.exam_list = ["piano", "guitar", "violin", "drums"]
        
    @catch_wrong_exam_name
    def add_abiturient(self, abiturient):
        for exam in self.exam_list:  
            if abiturient.instrument.lower() == exam:
                self.abiturients.append(abiturient)  
                return
        raise ValueError(f"No exam found for instrument '{abiturient.instrument}'.")

    def exam_participants(self, instrument):
        matching_abiturients = []
        for abiturient in self.abiturients:
            if abiturient.instrument == instrument:
                matching_abiturients.append(abiturient)
        return matching_abiturients

    def sort_by_name(self):
        sorted_abiturients = sorted(self.abiturients, key=lambda x: x.name)
        return sorted_abiturients
    
    def get_all_abiturients(self):
        abiturient_dict = {}
        for abiturient in self.abiturients:
            abiturient_dict[abiturient.name] = abiturient.instrument
        return abiturient_dict
    
    def get_abiturient_info(self, abiturient_name):
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