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

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

print(issubclass(Rectangle, Shape))  # True
print(issubclass(Circle, Shape))  # False

# Приклад використання функції issubclass для перевірки, чи кожен підклас наслідується від абстрактного класу