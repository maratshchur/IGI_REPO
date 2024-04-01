def decorator(func):
    def wrapper():
        print("Enter the value of x from (|x|<1): ")
        result, n = func()
        if (result and n):
            print(f"The result is: {result}")
            print(f"Number of iterations is: {n}")
    return wrapper