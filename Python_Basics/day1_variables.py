print("Python working successfully")
#VARIABLES 
name = "Sunny"
age = 20
college = "Galgotias University"
print(name)
print(age)
print(college)
#DATA TYPES 
height = 5.9
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
#Modify Variables
age = age + 1
print(age)
name = name + " Chaudhary"
print(name)
#Formatted Printing
print("My name is", name, "and I am", age, "years old")
print(f"My name is {name} and I am {age} years old")
#User Input
user_name = input("Enter your name: ")
print("Hello", user_name)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)

#fix it using integer conversion:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)

#Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)

#Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)

#Swap Variables
a = 5
b = 10

a, b = b, a
print(a, b)
