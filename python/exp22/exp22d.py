# Write a program to find the sum of the numbers for the elements of the list by using reduce()

from functools import reduce


def main():
    numbers = map(int, input("Enter the numbers separated by space: ").split())

    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    print("The sum of the numbers is: ", sum_of_numbers)


main()
