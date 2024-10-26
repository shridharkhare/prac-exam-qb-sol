def cel_to_fahr(celsius):
    return celsius * 9 / 5 + 32


def main():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = cel_to_fahr(celsius)
    print(f"The temperature in Fahrenheit is: {fahrenheit}")


main()
