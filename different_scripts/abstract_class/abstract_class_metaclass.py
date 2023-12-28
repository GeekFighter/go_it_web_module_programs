from abc import abstractmethod, ABCMeta


class MyBaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def baz(self):
        pass


class Child(MyBaseClass):
    def foo(self):
        print("Hello, foo")
    
    def baz(self):
        print("Hello, baz")


c = Child()
c.foo()
c.baz()