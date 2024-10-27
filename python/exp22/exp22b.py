# Write a program for filter() to filter only even numbers from a given list.


def main():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List of numbers: ", list_of_numbers)

    even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))
    print("Even numbers are: ", even_numbers)


main()
