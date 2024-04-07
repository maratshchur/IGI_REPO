def catch_wrong_exam_name(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print("Abiturient added succesfully")
        except ValueError as e:
            print(e)
    return wrapper