# Write a Python program to create a class to print the area of a square and a
# rectangle using Method overloading.


class Area:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def area(self, length, width):
        return length * width

    def area(self, length):
        return length * length


def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    obj = Area(length, width)
    print(f"Area of rectangle: {obj.area(length, width)}")

    obj = Area(length)
    print(f"Area of square: {obj.area(length)}")


main()
