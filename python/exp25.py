# Create a python program that checks if a number entered by the user is even or odd. Include custom error handling for non-integer inputs.


def main():
    input_number = input("Enter a number: ")
    try:
        number = int(input_number)
    except ValueError:
        print("Please enter a valid number.")
        return

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


main()
