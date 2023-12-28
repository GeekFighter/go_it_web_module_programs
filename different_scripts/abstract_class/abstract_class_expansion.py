from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speak())  # Виводить: "Woof!"
print(cat.speak())  # Виводить: "Meow!"
print(cow.speak())  # Виводить: "Moo!"