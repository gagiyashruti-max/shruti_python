a = "hello world"
print(a)

#2 Program to add two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print("Sum of the two numbers is:", result)

#3 Take input from the user
num = int(input("Enter a number: "))

#4 Check even or odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 5 PI value
    import math
print("PI value is:",math.pi)

# 6 store and constand

#6 constant
PI = 3.14159   # constant by convention

print(PI)

#7 Get user input
num = float(input("Enter a number: "))

# Calculate square
square = num ** 2

# Print the result
print(f"The square of {num} is {square}")

#8 Python program to calculate the area of a circle

import math  # for using pi

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

print("The area of the circle is:", area)

#9 Example variables
x = 10
y = 3.14
z = "Hello"
a = [1, 2, 3]
b = {"name": "Alice", "age": 25}

# Check their data types
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(a))  # <class 'list'>
print(type(b))  # <class 'dict'>

#10 math function
import math

# Square root
print(math.sqrt(16))  # Output: 4.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Trigonometry
print(math.sin(math.pi / 2))  # Output: 1.0

# Logarithm
print(math.log(100, 10))  # Output: 2.0

#11 Example: 2 to the power of 3
base = 2
exponent = 3
result = base ** exponent
print(result)  # Output: 8

# 12 Ask the user to enter a number
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

