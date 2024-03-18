from data import TEXT


def words_with_odd_number_of_letters(text):
    """
    Returns a list of words from the given text and a list of words with an odd number of letters.

    Args:
        text (str): The input text.

    Returns:
        tuple: A tuple containing two lists - words and odd_letter_words.
            - words (list): The list of all words in the text.
            - odd_letter_words (list): The list of words with an odd number of letters.
    """
    words = text.split(" ")
    odd_letter_words = []
    for word in words:
        letter_count = len(word.replace(",", "").replace(".", ""))
        if letter_count % 2 != 0:
            odd_letter_words.append(word)
    return words, odd_letter_words


def shortest_word_starts_with_i(words):
    """
    Finds the shortest word that starts with the letter 'i' from the given list of words.

    Args:
        words (list): The list of words.

    Returns:
        str: The shortest word starting with 'i'.
    """
    i_words = [word.strip(",.") for word in words if word.lower().startswith("i")]
    shortest_i_word = min(i_words, key=len, default=None)
    return shortest_i_word


def find_repeated_words(words):
    """
    Finds the repeated words from the given list of words.

    Args:
        words (list): The list of words.

    Returns:
        list: The list of repeated words.
    """
    unique_words = set(words)
    repeated_words = [word for word in unique_words if words.count(word) > 1]
    return repeated_words


def analyze_string():
    """
    Analyzes a string by performing various operations and printing the results.

    The function performs the following operations:
    1. Counts the number of words in the string and prints all words with an odd number of letters.
    2. Finds the shortest word that starts with the letter 'i' and prints it.
    3. Prints the repeated words in the string.

    Args:
        None

    Returns:
        None
    """
    text = TEXT

    # Count the number of words in the string and print all words with an odd number of letters
    words, odd_letter_words = words_with_odd_number_of_letters(text)
    print(f"Number of words: {len(words)}")
    print("Words with an odd number of letters:", ", ".join(odd_letter_words))

    # Find the shortest word that starts with the letter 'i'
    shortest_i_word = shortest_word_starts_with_i(words)
    print("Shortest word starting with 'i':", shortest_i_word)

    # Print repeated words
    repeated_words = find_repeated_words(words)
    print("Repeated words:", ", ".join(repeated_words))


def task4():
    analyze_string()