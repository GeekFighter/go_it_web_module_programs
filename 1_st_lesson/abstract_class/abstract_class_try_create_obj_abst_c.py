from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Implementation of abstract_method"

# Спроба створити екземпляр абстрактного класу
obj = AbstractClass()  # Генерує TypeError: Can't instantiate abstract class AbstractClass with abstract methods abstract_method

# Створення екземпляру підкласу
obj2 = ConcreteClass()
print(obj2.abstract_method())  # Виводить: "Implementation of abstract_method"