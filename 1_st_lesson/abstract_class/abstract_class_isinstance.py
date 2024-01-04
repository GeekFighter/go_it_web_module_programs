from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(4, 5), Circle(3), "Triangle"]

for shape in shapes:
    if isinstance(shape, Shape):
        print(f"Area of shape: {shape.area()}")
    else:
        print("Invalid shape")

# Приклад використання функції isinstance для перевірки, чи кожен елемент списку shapes є екземпляром класу, що наслідується від абстрактного класу.