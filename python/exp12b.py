def factorial(num):
    while num > 0:
        return num * factorial(num - 1)
    return 1


def main():
    num = int(input("Enter the number: "))
    print(f"The factorial of {num} is: {factorial(num)}")
