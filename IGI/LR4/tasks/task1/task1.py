from tasks.task1.models import Abiturient, Exam
from tasks.task1.output import print_task_options
from data import CSV_FILE_PATH, PICKLE_FILE_PATH
from tasks.task1.serializers import save_to_pickle, save_to_csv
from tasks.task1.deserializers import load_from_pickle

def task1():
    
    exam = Exam()
    
    
    
     
    while True:
        print_task_options()
        choice = input("Enter option: ")  
        if choice == '1':
            name = input("Enter name: ")
            instrument = input("Enter instrument (drums, guitar, violin, piano) ")
            abiturient = Abiturient(name, instrument)
            exam.add_abiturient(abiturient)

        elif choice == '2':
            exam_name = input("Enter exam to search: ")
            matching_abiturients = exam.exam_participants(exam_name)
            if matching_abiturients:
                print("Matched abiturients:")
                for abiturient in matching_abiturients:
                    print(f"Name: {abiturient.name}, Instrument: {abiturient.instrument}")
            else:
                print("No abiturients found for the specified exam.")

        elif choice == '3':
            save_to_csv(CSV_FILE_PATH, exam.get_all_abiturients())
            print("Abiturients saved to CSV successfully.")

        elif choice == '4':

            save_to_pickle(PICKLE_FILE_PATH, exam.get_all_abiturients())
            print("Abiturients saved to Pickle successfully.")

        elif choice == '5':
            matching_abiturients = exam.get_all_abiturients()
            if matching_abiturients:
                print("Abiturients:")
                for abiturient in matching_abiturients.keys():
                    print(f"Name: {abiturient}, Instrument: {matching_abiturients[abiturient]}")
            else:
                print("No abiturients found.")
            
        elif choice == '6':
            sorted_abiturients = exam.sort_by_name()
            print("Sorted abiturients by name:")
            for abiturients in sorted_abiturients:
                print(f"Name: {abiturients.name}, Instrument: {abiturients.instrument}")
                    
        elif choice == '7':
            break
            
        else:
            print("Invalid choice. Please try again.")
