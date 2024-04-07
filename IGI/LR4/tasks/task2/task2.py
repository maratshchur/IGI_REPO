from tasks.task2.models import TextAnalyzer
from tasks.task2.data import INPUT_TXT_PATH, OUTPUT_TXT_PATH
def task2():
    analyzer = TextAnalyzer(INPUT_TXT_PATH, OUTPUT_TXT_PATH)
    analyzer.read_text()
    analyzer.save_results()
    analyzer.archive_results()
    print("Text analised succesfully")