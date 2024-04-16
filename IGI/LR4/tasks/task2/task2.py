from tasks.task2.models import TextAnalyzer
from tasks.task2.data import INPUT_TXT_PATH, OUTPUT_TXT_PATH

#Задание №2 Вариант 28

# В соответствии с заданием своего варианта составить программу для анализа текста. Считать из исходного файла текст.
# Используя регулярные выражения получить искомую информацию (см. условие), вывести ее на экран и сохранить в другой файл.
# Заархивировать файл с результатом с помощью модуля zipfile и обеспечить получение информации о файле в архиве.
# Также выполнить общее задание – определить и сохранить в файл с результатами: 
# –	количество предложений в тексте; 
# –	количество предложений в тексте каждого вида отдельно (повествовательные, вопросительные и побудительные); 
# –	среднюю длину предложения в символах (считаются только слова); 
# –	среднюю длину слова в тексте в символах;
# –	количество смайликов в заданном тексте. Смайликом будем считать последовательность символов, удовлетворяющую условиям: 
#  первым символом является либо «;» (точка с запятой) либо «:» (двоеточие) ровно один раз; 
#  далее может идти символ «-» (минус) сколько угодно раз (в том числе символ минус может идти ноль раз); 
#  в конце обязательно идет некоторое количество (не меньше одной) одинаковых скобок из следующего набора: «(», «)», «[», «]»; 
#  внутри смайлика не может встречаться никаких других символов.
#  Например, эта последовательность является смайликом:
# «;---------[[[[[[[[». Эти последовательности смайликами не являются: «]», «;--»,«:»,«)».

# Получить список всех слов текста длиной менее 5 символов
# В заданной строке все пары символов, первый из которых – малая латинская буква, 
# а второй – большая латинская буква, выделить знаками «_?_» с обеих сторон.
# определить количество слов в строке и вывести на экран все
# слова, количество букв у которых четное;
# найти самое короткое слово, которое начинается на 'a';
# вывести повторяющиеся слова


def task2():
    analyzer = TextAnalyzer(INPUT_TXT_PATH, OUTPUT_TXT_PATH)
    analyzer.read_text()
    analyzer.save_results()
    print("Text analised succesfully")
    print(f"Results saved in {OUTPUT_TXT_PATH}")
    analyzer.archive_results()
    