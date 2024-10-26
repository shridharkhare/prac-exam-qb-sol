fd = dict()
l1 = list()
l2 = list()


def insert_key_value():
    print("Enter key value pair seperated by comma: ")
    key, value = input().split(",")
    fd.update({key: value})
    print("Updated dictionary is: ", fd)


def value_of(key):
    print(f"Value of {key} is {fd[key]}")


def map_list():
    print("Enter the elements of list1 seperated by comma: ")
    l1.extend(input().split(","))
    print("Enter the elements of list2 seperated by comma: ")
    l2.extend(input().split(","))
    print("Mapped dictionary is: ", dict(zip(l1, l2)))


def main():
    while True:
        print(
            "1. To insert key value pair"
            + "\n"
            + "2. To get value of a key"
            + "\n"
            + "3. To map two lists"
            + "\n"
            + "4. To exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert_key_value()
        elif choice == 2:
            key = input("Enter the key: ")
            value_of(key)
        elif choice == 3:
            map_list()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
