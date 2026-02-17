name = input("Enter your name: ")
print("Hello", name)
#Why int() needed
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)

#Fix Using Type Casting
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

#Mini Calculator
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

#Area of Circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area =", area)

#Age in Days
age = int(input("Enter age: "))
days = age * 365
print("You lived approx", days, "days")

#Temperature Converter
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)