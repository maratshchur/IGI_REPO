from abc import ABC, abstractmethod
import math
class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of a geometric figure.

        This method must be implemented by subclasses.

        Returns:
            float: The calculated area of the figure.
        """
        pass

class ShapeColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """
        The color property of a shape.

        Returns:
            str: The color of the shape.
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class RegularPentagon(GeometricFigure):
    def __init__(self, a, color):
        self.side_length = a
        self.color = ShapeColor(color)

    def calculate_area(self):
        """
        Calculates the area of the regular pentagon.

        Returns:
            float: The calculated area of the regular pentagon.
        """
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2

    def get_parameters(self):
        """
        Retrieves the parameters of the regular pentagon.

        Returns:
            str: A string representation of the regular pentagon's parameters.
        """
        
        return "Shape: Regular Pentagon, Side Length: {}, Color: {}, Area: {}".format(
            self.side_length, self.color._color, self.calculate_area()
        )
        
    def get_pentagon_coordinates(self, side_length):
        """
        Calculates the coordinates of the vertices of a regular pentagon.

        Args:
            side_length (float): The side length of the regular pentagon.

        Returns:
            tuple: A tuple containing two lists of x and y coordinates respectively.
        """
        x_coordinates = []
        y_coordinates = []
        radius = side_length / (2 * math.sin(math.pi / 5))  
        angle = math.pi / 2  

        for _ in range(5):
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            x_coordinates.append(x)
            y_coordinates.append(y)
            angle += 2 * math.pi / 5  # Увеличение угла на 2π/5

        return x_coordinates, y_coordinates

