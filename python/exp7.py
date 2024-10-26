def inputstr():
    str1 = input("Enter the first string: ").lower().strip()
    str2 = input("Enter the second string: ").lower().strip()
    return str1, str2


def common_characters(str1_set, str2_set):
    common = str1_set & str2_set
    print("Common characters are: ", common)


def difference_characters(str1_set, str2_set):
    difference = str1_set - str2_set
    print("Characters in string 1 but not in string 2 are: ", difference)


def union_characters(str1_set, str2_set):
    union = str1_set | str2_set
    print("Union of characters are: ", union)


def symmetric_difference_characters(str1_set, str2_set):
    symmetric_difference = str1_set ^ str2_set
    print("Symmetric difference of characters are: ", symmetric_difference)


def main():
    while True:
        print(
            "1. To input strings"
            + "\n"
            + "2. To find common characters"
            + "\n"
            + "3. To find difference characters"
            + "\n"
            + "4. To find union characters"
            + "\n"
            + "5. To find symmetric difference characters"
            + "\n"
            + "6. To exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            str1, str2 = inputstr()
            str1_set = set(str1)
            str2_set = set(str2)
        elif choice == 2:
            common_characters(str1_set, str2_set)
        elif choice == 3:
            difference_characters(str1_set, str2_set)
        elif choice == 4:
            union_characters(str1_set, str2_set)
        elif choice == 5:
            symmetric_difference_characters(str1_set, str2_set)
        elif choice == 6:
            break
        else:
            print("Invalid choice")


main()
