from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    pass

dog = Dog()
cat = Cat()
bird = Bird()  # Генерує TypeError: Can't instantiate abstract class Bird with abstract methods make_sound