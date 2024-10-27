fd = dict()
l1 = list()
l2 = list()


def insert_key_value():
    print("Enter key value pair seperated by comma: ")
    key, value = input().split(",")
    fd.update({key: value})
    print("Updated dictionary is: ", fd)


def update_key_value():
    print("Enter key value pair seperated by comma: ")
    key, value = input().split(",")
    fd.update({key: value})
    print("Updated dictionary is: ", fd)


def map_list():
    print("Mapped dictionary is: ", dict(zip(l1, l2)))


def main():
    while True:
        print(
            "1. To insert key value pair"
            + "\n"
            + "2. To update key value pair"
            + "\n"
            + "3. To map two lists"
            + "\n"
            + "4. To exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert_key_value()
        elif choice == 2:
            update_key_value()
        elif choice == 3:
            print("Enter the elements of list1 seperated by comma: ")
            l1.extend(input().split(","))
            print("Enter the elements of list2 seperated by comma: ")
            l2.extend(input().split(","))
            map_list()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
