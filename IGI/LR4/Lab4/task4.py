import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from abc import ABC, abstractmethod

def task4():
    while True:
        try:
            figure_type = input("Enter figure type (rectangle, parallelogram): ")
            if figure_type.lower() not in ['rectangle', 'parallelogram']:
                raise ValueError
            color = input("Enter color: ")
            text = input("Enter text: ")
            if figure_type.lower() == 'rectangle':
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                rectangle = Rectangle(width, height, color)
                print(rectangle)
                rectangle.draw(text)
            elif figure_type.lower() == 'parallelogram':
                d1 = float(input("Enter diagonal 1: "))
                d2 = float(input("Enter diagonal 2: "))
                angle = float(input("Enter angle (in degrees): "))
                parallelogram = Parallelogram(d1, d2, angle, color)
                print(parallelogram)
                parallelogram.draw(text)
            break
        except ValueError:
            print("Invalid input. Please try again.")
class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

class ColorMixin:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Rectangle(GeometricFigure, ColorMixin):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width}, height {self.height}, color {self.color}, and area {self.area()}"

    def draw(self, text):
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((0, 0), self.width, self.height, fc=self.color)
        ax.add_patch(rectangle)
        plt.text(self.width / 2, self.height / 2, text, ha='center', va='center', color='white')
        plt.axis('scaled')
        plt.show()

class Parallelogram(GeometricFigure, ColorMixin):
    def __init__(self, d1, d2, angle, color):
        super().__init__(color)
        self.d1 = d1
        self.d2 = d2
        self.angle = math.radians(angle)

    def area(self):
        return self.d1 * self.d2 * math.sin(self.angle)

    def __str__(self):
        return f"Parallelogram with diagonals {self.d1} and {self.d2}, angle {math.degrees(self.angle)} degrees, color {self.color}, and area {self.area()}"

    def draw(self, text):
        fig, ax = plt.subplots()
        x = [0, self.d1, self.d1 + self.d2 * math.cos(self.angle), self.d2 * math.cos(self.angle)]
        y = [0, 0, self.d2 * math.sin(self.angle), self.d2 * math.sin(self.angle)]
        parallelogram = Polygon(list(zip(x, y)), fc=self.color)
        ax.add_patch(parallelogram)
        plt.text(self.d1 / 2, self.d2 * math.sin(self.angle) / 2, text, ha='center', va='center', color='white')
        plt.axis('scaled')
        plt.show()