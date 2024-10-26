import os


def count_lwc(filename):
    with open(filename, "r") as f:
        f = f.readlines()

    lines = len(f)
    words = 0
    chars = 0

    for line in f:
        words += len(line.split())
        chars += len(line)

    return lines, words, chars


def count_of_files():
    files = os.listdir()
    count = 0
    for file in files:
        count += 1
    return count


def main():
    filename = "exp18.txt"

    lines, words, chars = count_lwc(filename)
    print(f"Lines: {lines}")
    count = count_of_files()
    print(f"Files: {count}")


main()
