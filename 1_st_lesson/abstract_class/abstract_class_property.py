from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @property
    @abstractmethod
    def abstract_property(self):
        pass

class MyClass(MyAbstractClass):
    @property
    def abstract_property(self):
        return "This is the implementation of abstract_property in MyClass"

# Не можна створювати екземпляр абстрактного класу
# abstract_class = MyAbstractClass()  # Видасть TypeError

my_class = MyClass()
print(my_class.abstract_property)  # Виводить: "This is the implementation of abstract_property in MyClass"