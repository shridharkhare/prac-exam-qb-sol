import math


def main():
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    print("Area of the circle is: ", area)
    print("Circumference of the circle is: ", circumference)


main()
