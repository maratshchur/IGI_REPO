from abc import ABC, abstractmethod
import math
class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class ShapeColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class RegularPentagon(GeometricFigure):
    def __init__(self, a, color):
        self.side_length = a
        self.color = ShapeColor(color)

    def calculate_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2

    def get_parameters(self):
        return "Shape: Regular Pentagon, Side Length: {}, Color: {}, Area: {}".format(
            self.side_length, self.color, self.calculate_area()
        )
        
    def get_pentagon_coordinates(self, side_length):
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

