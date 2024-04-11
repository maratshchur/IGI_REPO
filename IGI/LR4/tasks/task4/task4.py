from tasks.task4.models import RegularPentagon
from additional_options.validation import validate_float_value, validate_figure_parameters
from tasks.task4.output import print_task_options
from tasks.task4.data import PICTURE_PATH
import matplotlib.pyplot as plt

#Задание №4 Вариант 28

# В соответствии с заданием своего варианта разработать базовые классы и классы наследники. 
# Требования по использованию классов:
# Абстрактный класс «Геометрическая фигура» содержит абстрактный метод для вычисления площади фигуры 
# (https://docs.python.org/3/library/abc.html )
# Класс «Цвет фигуры» содержит свойство для описания цвета геометрической фигуры 
# (https://docs.python.org/3/library/functions.html#property )
# Класс «Прямоугольник» (Круг, Ромб, Квадрат, Треугольник и т.д.)
# наследуется от класса «Геометрическая фигура».
# Класс должен содержать конструктор по параметрам «ширина», «высота» 
# (для другого типа фигуры соответствующие параметры, например, для круга задаем «радиус») 
# и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета. 
# Класс должен переопределять метод, вычисляющий площадь фигуры https://docs.python.org/3/library/math.html .
# Для класса «Прямоугольник»(тип фигуры в инд. задании) 
# определить метод, который возвращает в виде строки основные параметры фигуры, ее цвет и площадь.
# Использовать метод format (https://pyformat.info/ )
# название фигуры должно задаваться в виде поля данных класса и возвращаться методом класса.
# В корневом каталоге проекта создайте файл main.py для тестирования классов.
# Используйте конструкцию, описанную в https://docs.python.org/3/library/__main__.html 
# Пример объекта: Прямоугольник синего цвета шириной 5 и высотой 8.
# Программа должна содержать следующие базовые функции:
# 1)	ввод значений параметров пользователем;
# 2) проверка корректности вводимых данных;
# 3) построение, закрашивание фигуры в выбранный цвет, введенный с клавиатуры,
# и подпись фигуры текстом, введенным с клавиатуры;
# 4) вывод фигуры на экран и в файл.

# Построить правильный пятиугольник со стороной a.

def input_parameters():
    """
    Function prompts the user for parameters of a regular pentagon.

    Returns:
        tuple: A tuple containing the side length of the pentagon (side_length) and the color (color).
    """
    side_length = input("Enter the side length of the regular pentagon: ")
    side_length = validate_float_value(side_length)
    color = input("Enter the color of the regular pentagon: ")
    return side_length, color

def draw_shape(shape, shape_color, text):
    """
    Function draws a shape on a plot using the matplotlib library.

    Args:
        shape (object): The shape object that has a get_pentagon_coordinates() method to obtain the vertex coordinates.
        shape_color (str): The color of the shape in a format supported by the matplotlib library.
        text (str): The text that will be placed next to the shape.

    Returns:
        None
    """
    fig, ax = plt.subplots()

    x_coords, y_coords = shape.get_pentagon_coordinates(shape.side_length)
    
    try:
        ax.fill(x_coords, y_coords, color=shape_color)
    except Exception as e:
        print("An error occurred while filling the shape:", str(e))
        return

    ax.text(min(x_coords), max(y_coords), text, fontsize=8)
    plt.savefig(PICTURE_PATH)
    plt.show()


def task4():
    side_length, color = input_parameters()
    if not validate_figure_parameters(side_length, color):
        print("Invalid input parameters.")
        return
    pentagon = RegularPentagon(side_length, color)
    text = input("Enter the text for the shape: ")
    draw_shape(pentagon, pentagon.color.color, text)
    print(pentagon.get_parameters())