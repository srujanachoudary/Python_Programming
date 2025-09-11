from abc import ABC,abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print('area of rectangle: ',a)

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=math.pi*self.radius**2
        print("area of circle : ",a)

rec=Rectangle(3,4)
rec.area()
cir=Circle(3.5)
cir.area()
