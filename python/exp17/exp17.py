def append_data(data, filename):
    with open(filename, "a") as f:
        f.write(data)
        f.write("\n")


def display_data(filename):
    with open(filename, "r") as f:
        f = f.readlines()
    for line in f:
        print(line, end="")


def count(filename):
    with open(filename, "r") as f:
        f = f.readlines()
    lines = len(f)
    words = 0
    chars = 0

    for line in f:
        words += len(line.split())
        chars += len(line)

    return lines, words, chars


def main():
    filename = "exp17.txt"
    data = input("Enter data: ")
    append_data(data, filename)
    display_data(filename)
    lines, words, chars = count(filename)
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")


main()
