# Write a python program to implement a function that checks if a number is prime and returns a list of all prime numbers up to a given limit


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_till(num):
    return list(filter(is_prime, range(num)))


def main():
    number = int(input("Enter a number: "))
    (
        print("Entered number is prime.")
        if is_prime(number)
        else print("Entered number is not prime.")
    )
    print("Prime numbers till", number, "are: ", prime_till(number))


main()
