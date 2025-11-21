class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


# Example usage
r1 = Rectangle(5, 4)
r2 = Rectangle(6, 3)

if r1 < r2:
    print("Rectangle r1 has smaller area than r2")
else:
    print("Rectangle r1 has larger or equal area than r2")
