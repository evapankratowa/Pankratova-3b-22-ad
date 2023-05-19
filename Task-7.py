class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width


square_1 = Rectangle(5, 20)
print(square_1.area())
