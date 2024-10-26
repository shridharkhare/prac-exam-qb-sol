# number list
temp_lst = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, "Python"]


def update_1_del_middle():
    inpt = input("Enter the element to be update in the first place:")
    temp_lst[0] = inpt
    del temp_lst[len(temp_lst) // 2]


def add_elements():
    names = list(input("Enter the names to be added seperated by comma:").split(","))
    temp_lst.extend(names)
    if "Python" in temp_lst:
        print("Python is present in the list")
    else:
        print("Python is not present in the list")


def main():
    while True:
        print(
            "1. To update first element and delete middle element"
            + "\n"
            + "2. To add elements to the list"
            + "\n"
            + "3. To exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            update_1_del_middle()
            print(temp_lst)
        elif choice == 2:
            add_elements()
            print(temp_lst)
        elif choice == 3:
            break
        else:
            print("Invalid choice")


main()
