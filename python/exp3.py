# list of random numbers
numbers = []
even = []
odd = []


def enter_numbers():
    numbers.clear()
    for i in range(10):
        num = int(input(f"Enter {i+1} number: "))
        numbers.append(num)


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def seperate_into_even_odd():
    even.clear()
    odd.clear()
    for num in numbers:
        if is_even(num):
            even.append(num)
        else:
            odd.append(num)


def merge_and_sort():
    new_list = even + odd
    new_list.sort()
    print("New list after merging and sorting:", new_list)


def min_max():
    print("Minimum number is:", min(numbers))
    print("Maximum number is:", max(numbers))


def main():
    while True:
        print(
            "1. To enter numbers"
            + "\n"
            + "2. To seperate into even and odd numbers"
            + "\n"
            + "3. To merge and sort"
            + "\n"
            + "4. To find minimum and maximum"
            + "\n"
            + "5. To exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            enter_numbers()
        elif choice == 2:
            seperate_into_even_odd()
        elif choice == 3:
            merge_and_sort()
        elif choice == 4:
            min_max()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
