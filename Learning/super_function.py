# super() = function used to give access to the methods of a parents class.
#           Returns a temporary object of a parent class when used.

number = 3

class Rectangle:
    pass
    def __init__(self, length, width, height, obj):
        self.length = length
        self.width = width
        self.height = height
        self.obj = obj
# In this section must be normal self

class Square(Rectangle):
    def __init__(self,length,width,height,obj):
        super().__init__(length,width,height,obj)
    def area(self):
        return self.length*self.width*self.height*self.obj
#square

class Cube(Rectangle):

    def __init__(self,length,width,height, obj):
        super().__init__(length, width, height, obj)
    def volume(self):
        return self.obj
#cube

square = Square(3,3,3,3).area() #area zwraca return
cube = Cube(3,3,3,9).volume() #volume zwraca return

print(square)

# OUTPUT = 81 >> (return self.length*self.width*self.height*self.obj)

print(cube)

# OUTPUT = 9 >> (return self.obj)