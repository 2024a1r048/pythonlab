 #Instance methods: Rectangle area and perimeter
"""
Problem: Create a Rectangle class with length and breadth.Use instance methods to calculate its area and perimeter.
"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10, 5)

print("Area of Rectangle:", r1.area())
print("Perimeter of Rectangle:", r1.perimeter())
