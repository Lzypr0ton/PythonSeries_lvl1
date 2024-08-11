# Python is capable of performing simple arithmetic operations such as
print(3 + 7)
print(3 - 7)
print(3 * 7)
print(3 / 7)

# Parentheses, Square Brackets, and Curly Braces in Python are mostly used to solve complex equations. It makes it easier for the compiler and provides accurate output.
result1 = True or False and False
print("Result without parentheses:", result1)
result2 = (True or False) and False
print("Result with parentheses:", result2)

# Now let's see how number-to-string conversion works
num = 1
print(1, "is my fav number")  # Great! Now let's convert num to a string

# print(num + "is my fav number")  # Oh, error! Why?
print(str(num) + " is my fav number")

# The following is used to find power values like 2^2, etc.
print(pow(2, 2))  # 4
print(pow(2, 3))  # 8
print(pow(2, 4))  # 16

print(min(6, 9))  # Prints the minimum number
print(max(6, 9))  # Prints the maximum number

print(round(69.34567))  # Prints the rounded figure of the number

# Now there is a module called math which has all math-related operations coded
import math
from math import *

num = 3.99
print(floor(num))  # Gives the floor value (decimal value with round figure)
print(ceil(num))  # Gives the ceiling value (decimal value with round figure)
print(sqrt(4))  # Displays the square root of the given number
