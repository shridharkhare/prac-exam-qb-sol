class Rectangle:
    length = 0
    width = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print(
            f"Width: {self.width}, Height: {self.height}, Area: {self.area()}, Perimeter: {self.perimeter()}"
        )


def main():
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    rect = Rectangle(width, height)
    rect.display()


main()
