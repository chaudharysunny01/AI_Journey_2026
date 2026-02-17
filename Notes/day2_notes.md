1. Why input() gives string?

In Python, the input() function always takes the value from keyboard as text (string).

This happens because the computer cannot guess what the user is entering.
For example, if a user types:

10

Python does not know whether it is:

a number for calculation

a phone number

a roll number

or just text

So Python safely stores it as a string.

Therefore:

input() returns string by default because user input is first treated as plain text.

Example:

a = input("Enter number: ")
print(type(a))

Output:

<class 'str'>

2. Why int() or float() is needed?

Since input() gives string, we cannot perform mathematical operations on it.

Example:

age = input("Enter age: ")
print(age + 5)

This gives error because Python cannot add number to text.

So we convert the string into numeric type.

int() → converts into whole number

float() → converts into decimal number

Example:

age = int(input("Enter age: "))
print(age + 5)

Therefore:

int() or float() is used to convert string input into numeric value so calculations can be performed.

3. Difference between int and float
   int float
   Stores whole numbers Stores decimal numbers
   No fraction allowed Fraction allowed
   Example: 5, 10, -2 Example: 3.14, 7.5
   Uses less memory Uses more memory
   Faster calculations Slightly slower calculations

Example:

a = 5 # int
b = 5.0 # float

So:

int is for whole numbers, while float is for numbers with decimal point.

# Short Revision

input() → always string

int()/float() → convert into number

int → whole number

float → decimal number
