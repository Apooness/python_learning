from abc import ABC, abstractmethod 
class Shape(ABC):
    
    @abstractmethod
    def Area(self): pass
    @abstractmethod
    def Perimeter(self): pass 

    def toString(self): pass

class Square(Shape):
    def __init__(self,edge):
        self.__edge = edge

    def Area(self):
        result = self.__edge**2
        print(result)

    def Perimeter(self):
        result = self.__edge*4
        print(result)

    def toString(self):
        print("Square is awesome")

class Circle(Shape):
    PI = 3.14

    def __init__(self,radius):
        self.__radius = radius

    def Area(self):
        result = self.PI * (self.__radius**2)
        print(result)

    def Perimeter(self):
        result = 2*self.PI*self.__radius
        print(result)

s = Square(5)
s.Area()
s.Perimeter()
s.toString()

c = Circle(10)
c.Area()
# c.Perimeter()
c.toString()