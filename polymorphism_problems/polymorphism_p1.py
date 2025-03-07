class Shape:

    def calculate_area(self):
        return "Undefined"

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return f" Area Of Circle - {3.14* self.radius**2}"


class Triangle (Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return f" Area Of Triangle - {self.height*self.base}"

class Rectangle (Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return f" Area  Of Rectangle- {self.length*self.width}"

shape =[Triangle(5,4),Circle(3),Rectangle(7,8)]
for shape in shape:
    print(shape.calculate_area())