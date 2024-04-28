import copy


class Shape:
    def __init__(self, **kwargs):
        self.type = kwargs.get("type", "Abstract Shape")

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.type = "Rectangle"
        self.width = width
        self.height = height

    def __str__(self):
        return f"Type: {self.type}, Width: {self.width}, Height: {self.height}"

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.type = "Circle"
        self.radius = radius

    def __str__(self):
        return f"Type: {self.type}, Radius: {self.radius}"

    def area(self):
        return 3.14 * self.radius**2


# Client code
if __name__ == "__main__":
    rectangle_prototype = Rectangle(width=10, height=5, color="blue")
    circle_prototype = Circle(radius=7, color="red")

    # Clone the prototypes
    rectangle_clone = rectangle_prototype.clone()
    circle_clone = circle_prototype.clone()

    # Modify the clones if needed
    rectangle_clone.width = 15
    circle_clone.radius = 5

    # Output the clones
    print(rectangle_clone)  # Output: Type: Rectangle, Width: 15, Height: 5
    print(rectangle_clone.area())  # Output: 75.0
    print(circle_clone)  # Output: Type: Circle, Radius: 5
    print(circle_clone.area())  # Output: 78.5
