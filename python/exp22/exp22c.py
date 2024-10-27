# Write a program for map() function to double all the items in the list.


def main():
    numbers = map(int, input("Enter the numbers separated by space: ").split())

    doubled_numbers = list(map(lambda x: x * 2), numbers)
    print("Doubled numbers are: ", doubled_numbers)


main()
