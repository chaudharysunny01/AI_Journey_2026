#VARIABLES
a variable is like a container or box that holds some value, and this value can change during program execution.

age = 19
name = "Sunny"
Here:

age is a variable storing number 19

name is a variable storing text Sunny

#DATA TYPES
A data type tells the computer what kind of value a variable is storing.
Common Data Types in Python
Data Type Meaning Example
int Integer (whole number) 5, 10, -2
float Decimal number 3.14, 7.5
str String (text) "Hello"
bool True or False True

Example:
x = 10 # int
y = 2.5 # float
name = "Ram"
#Why int() is Needed
In Python, when we take input from user using input() function,
the value is always taken as string (text) by default.

Example:

age = input("Enter your age: ")
print(age + 5)

If user enters 19, Python treats it as "19" (text),
and we cannot add number to text → error.
age = int(input("Enter your age: "))
print(age + 5)
Now Python understands it as number and performs addition.

Therefore:

int() is used to convert string input into integer so that mathematical operations can be performed.
