def check_str_palindrome():
    og_str = input("Enter a string to check if it is a palindrome: ").lower().strip()

    if og_str == og_str[::-1]:
        print("The Entered string is a palindrome.")
    else:
        print("The entered string is not a palindrome.")


def check_int_palindrome():
    og_number = input("Enter a number to check palindrome: ")
    num = og_number

    rev = 0
    while num != 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10

    if rev == og_number:
        print("Entered number is a palindrome.")
    else:
        print("Entered number is not a plaindrome")


def main():
    while True:
        print(
            "1. Check whether a number is palindrome:  \n 2. Check whether a string is palindrome \n 3. Exit \n"
        )
        choice = int(input("Enter a choice: "))

        if choice == 1:
            check_int_palindrome()
        elif choice == 2:
            check_str_palindrome()
        elif choice == 3:
            break
        else:
            print("Invalid Input")


main()
