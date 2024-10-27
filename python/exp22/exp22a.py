# Write a program to double a given number and add two numbers using
# lambda()?

x, y = int(input("Enter two numbers: ").split())

double = lambda x: x * 2
add = lambda x, y: x + y

x = double(x)
y = double(y)

print("The sum of double of both numbers is, ", add(x, y))
