# Define the Shape class
class Shape:
    # Initialize the class with the number of sides as an argument (default is 0)
    def __init__(self, sides=0):
        # Store the number of sides as an instance variable
        self.sides = sides

    # Define an abstract method for the area of the shape
    def area(self):
        # This method should be overridden in the subclass
        pass

    # Define an abstract method for the perimeter of the shape
    def perimeter(self):
        # This method should be overridden in the subclass
        pass


# Define the Square class, which inherits from the Shape class
class Square(Shape):
    # Initialize the class with the length of one side as an argument
    def __init__(self, length):
        # Call the parent class's __init__ method to set the number of sides to 4
        super().__init__(4)
        # Store the length as an instance variable
        self.length = length

    # Override the area method to calculate the area of the square
    def area(self):
        return self.length**2

    # Override the perimeter method to calculate the perimeter of the square
    def perimeter(self):
        return self.length * 4


# Define the Circle class, which inherits from the Shape class
class Circle(Shape):
    # Initialize the class with the radius as an argument
    def __init__(self, radius):
        # Call the parent class's __init__ method with no argument to set the number of sides to 0
        super().__init__()
        # Store the radius as an instance variable
        self.radius = radius

    # Override the area method to calculate the area of the circle
    def area(self):
        return 3.14 * self.radius**2

    # Override the perimeter method to calculate the circumference of the circle
    def perimeter(self):
        return 2 * 3.14 * self.radius


# Create a Square object with length 5
square = Square(5)
# Print the area and perimeter of the square
print("Square:")
print("Area:", square.area())
print("Perimeter:", square.perimeter())

# Create a Circle object with radius 5
circle = Circle(5)
# Print the area and perimeter of the circle
print("\nCircle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
