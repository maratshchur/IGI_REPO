# Program Name: IGI Laboratory work №3
# Program Version: 1.0
# Developer: Marat Shchur
# Date: 2024-03-07


# ToDo: add decorator 
from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3
from tasks.task4 import task4
from tasks.task5 import task5

from additional_options.choose_options import choose_task_number
from additional_options.validation import validate_int_value
from additional_options.choose_options import continue_program_request


def main():

    while True:
        task_number = choose_task_number()
        task_number = validate_int_value(task_number)
        if task_number==1:
            task1()
        elif task_number==2:
            task2()  
        elif task_number==3:
            task3()
        elif task_number==4:
            task4()
        elif task_number==5:
            task5()       
        else:
            print("Incorrect input, try again")
            continue
        choose = continue_program_request()
        if not choose:
            print("Exiting the program.")
            return

if __name__ == "__main__":
    main()
    
