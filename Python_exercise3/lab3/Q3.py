"""
Yinglin Lu 2212059

class encapsulation/properties/Inheritance/method overriding/chaining
Nov 12, 2022
This is Q3
"""
from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, model, cylinder):
        self.__model = model
        self.__cylinder = cylinder
        self.__name = ""

    @property
    def model(self):
        return self.__model

    @property
    def cylinder(self):
        return self.__cylinder

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        ...

    @abstractmethod
    def break_(self):
        ...

    def __str__(self):
        return f"Name:{self.name:<20s}Model:{self.model:<20s}Cylinder:{self.cylinder:<20d}"


class Mazda(Auto):
    def __init__(self, model, cylinder):
        super().__init__(model, cylinder)
        self.name = "Mazda"

    def start(self):
        print(f"{self.name} start engine...")
        return self

    def accelerate(self):
        print(f"{self.name} accelerate ...")
        return self

    def break_(self):
        print(f"{self.name} break...")
        return self


class BMW(Auto):
    def __init__(self, model, cylinder):
        super().__init__(model, cylinder)
        self.name = "BMW"

    def start(self):
        print(f"{self.name} start engine...")
        return self

    def accelerate(self):
        print(f"{self.name} accelerate ...")
        return self

    def break_(self):
        print(f"{self.name} break...")
        return self


class Lamborghini(Auto):
    def __init__(self, model, cylinder):
        super().__init__(model, cylinder)
        self.name = "Lamborghini"

    def start(self):
        print(f"{self.name} start engine...")
        return self

    def accelerate(self):
        print(f"{self.name} accelerate ...")
        return self

    def break_(self):
        print(f"{self.name} break...")
        return self


mazda = Mazda("CX-7", 4)
bmw = BMW("M2", 6)
lamborghini = Lamborghini("aventador", 8)

for car in (mazda, bmw, lamborghini):
    print(car)
    car.start().accelerate().break_()
    print("\n")
