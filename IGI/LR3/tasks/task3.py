def analyze_text(text):
    """
    Analyzes the text input from the keyboard and counts the number of lowercase letters and digits.

    Returns:
        None
    """
    lowercase_count = 0
    digit_count = 0

    for char in text:
        if char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
    return lowercase_count, digit_count

    


def task3():
    text = input("Enter text: ")
    lowercase_count, digit_count = analyze_text(text)
    print(f"Number of lowercase letters: {lowercase_count}")
    print(f"Number of digits: {digit_count}")