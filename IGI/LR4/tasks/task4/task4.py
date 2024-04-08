from tasks.task4.models import RegularPentagon
from additional_options.validation import validate_float_value, validate_figure_parameters
from tasks.task4.output import print_task_options
from tasks.task4.data import PICTURE_PATH
import matplotlib.pyplot as plt

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