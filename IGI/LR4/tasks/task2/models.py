import re
import zipfile
from collections import Counter
from tasks.task2.data import ZIP_FILE_PATH

class TextAnalyzer:
    """
    A class for analyzing text data.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.

    Attributes:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.

    Methods:
        read_text: Read the text from the input file.
        count_sentence_types: Count the sentence types.
        count_sentences: Count the total number of sentences.
        calculate_average_sentence_length: Calculate the average sentence length.
        calculate_average_word_length: Calculate the average word length.
        count_smileys: Count the number of smileys.
        find_short_words: Find and return short words.
        modify_text: Modify the text.
        count_words: Count the total number of words.
        find_even_length_words: Find and return words with even length.
        find_shortest_a_word: Find and return the shortest word starting with 'a'.
        find_repeated_words: Find and return repeated words.
        save_results: Save the analysis results.
        archive_results: Create a zip archive.

    """
    def __init__(self, input_file, output_file):
        """
        Initialize a TextAnalyzer instance.

        Args:
            input_file (str): Path to the input file containing the text to analyze.
            output_file (str): Path to the output file where the analysis results will be saved.

        """    
        self.input_file = input_file
        self.output_file = output_file
        self.text = None
        self.sentences = None
        self.words = None
        self.smileys = None
        self.short_words = None
        self.modified_text = None
        self.word_counts = None

    def read_text(self):
        """
        Read the text from the input file.

        """
        with open(self.input_file, 'r') as file:
            self.text = file.read()

    def count_sentence_types(self):
        """
        Count the number of narrative, interrogative, and imperative sentences in the text.

        Returns:
            tuple: A tuple containing the counts of narrative, interrogative, and imperative sentences.

        """
        narrative_sentences = re.findall(r'[A-Z][^.!?]*\.', self.text)
        narrative_sentences += re.findall(r'[A-Z][^.!?]*\.{3}', self.text)
        interrogative_sentences = re.findall(r'[A-Z][^.!?]*\?', self.text)
        imperative_sentences = re.findall(r'[A-Z][^.!?]*!', self.text)
        return len(narrative_sentences), len(interrogative_sentences), len(imperative_sentences)

    def count_sentences(self):
        """
        Count the total number of sentences in the text.

        Returns:
            int: The number of sentences in the text.

        """
        lengths=self.count_sentence_types()
        self.sentences = 0
        for number in lengths:
            self.sentences+=number
        return self.sentences
    
    def calculate_average_sentence_length(self):
        """
        Calculate the average length of sentences in characters.

        Returns:
            float: The average sentence length in characters.

        """
        self.words = re.findall(r'\b\w+\b', self.text)
        total_chars_per_sentence = sum(len(word) for word in self.words)
        return total_chars_per_sentence / self.sentences

    def calculate_average_word_length(self):
        """
        Calculate the average length of words in characters.

        Returns:
            float: The average word length in characters.

        """
        total_chars_per_word = sum(len(word) for word in self.words)
        return total_chars_per_word / len(self.words)

    def count_smileys(self):
        """
        Count the number of smileys in the text.

        Returns:
            int: The number of smileys in the text.

        """
        self.smileys = re.findall(r'([:;]-*([()\[\]])\2*)', self.text)
        return len(self.smileys)

    def find_short_words(self):
        """
        Find and return a list of words with less than 5 characters.

        Returns:
            list: A list of words with less than 5 characters.

        """
        self.short_words = [word for word in self.words if len(word) < 5]
        return self.short_words

    def modify_text(self):
        """
        Modify the text by highlighting character pairs.

        Returns:
            str: The modified text.

        """
        self.modified_text = re.sub(r'([a-z])([A-Z])', r'?\1\2?', self.text)
        return self.modified_text

    def count_words(self):
        """
        Count the total number of words in the text.

        Returns:
            int: The number of words in the text.

        """
        self.word_counts = Counter(self.words)
        return len(self.words)

    def find_even_length_words(self):
        """
        Find and return a list of words with an even number of letters.

        Returns:
            list: A list of words with an even number of letters.

        """
        return [word for word in self.word_counts if len(word) % 2 == 0]

    def find_shortest_a_word(self):
        pattern = r'\ba\w*\b'
        matches = re.findall(pattern, self.text)
    
        shortest_word = None
        for word in matches:
            if shortest_word is None or len(word) < len(shortest_word):
                shortest_word = word
    
        return shortest_word

    def find_repeated_words(self):
        """
        Find and return a list of words that appear more than once in thetext.

        Returns:
            list: A list of words that appear more than once in the text.

        """
        return [word for word, count in self.word_counts.items() if count > 1]

    def save_results(self):
        """
        Save the analysis results to the output file.

        """
        with open(self.output_file, 'w') as file:
            file.write(f"Number of sentences in the text: {self.count_sentences()}\n")
            narrative, interrogative, imperative = self.count_sentence_types()
            file.write(f"Number of narrative sentences: {narrative}\n")
            file.write(f"Number of interrogative sentences: {interrogative}\n")
            file.write(f"Number of imperative sentences: {imperative}\n")
            file.write(f"Average sentence length (in characters): {self.calculate_average_sentence_length()}\n")
            file.write(f"Average word length (in characters): {self.calculate_average_word_length()}\n")
            file.write(f"Number of smileys: {self.count_smileys()}\n")
            file.write("List of words with less than 5 characters:\n")
            file.write(' '.join(self.find_short_words()))
            file.write("\n\n")
            file.write("Original text with highlighted character pairs:\n")
            file.write(self.modify_text())
            file.write("\n\n")
            file.write(f"Number of words in the text: {self.count_words()}\n")
            file.write("Words with an even number of letters:\n")
            file.write(' '.join(self.find_even_length_words()))
            file.write("\n\n")
            file.write(f"Shortest word starting with 'a': {self.find_shortest_a_word()}\n")
            file.write("Repeated words:\n")
            file.write(' '.join(self.find_repeated_words()))

    def archive_results(self):
        """
        Create a zip archive containing the output file.

        """
        with zipfile.ZipFile(ZIP_FILE_PATH, 'w') as zip_file:
            zip_file.write(self.output_file)
