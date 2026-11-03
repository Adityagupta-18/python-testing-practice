from math import pi

class Shapes():
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius


class Rectangle(Shapes):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)
