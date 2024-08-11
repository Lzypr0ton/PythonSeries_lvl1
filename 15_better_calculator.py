# Taking input from user for num1, operator, and num3
a = float(input("Enter num1: "))  # Converting input to float for numerical operations
b = input("Enter the operator: ")  # Operator input (can be +, -, *, /)
c = float(input("Enter num3: "))  # Converting input to float for numerical operations

# Performing arithmetic operations based on the operator
if b == "+":
    print(a + c)  # Addition
elif b == "-":
    print(a - c)  # Subtraction
elif b == "*":
    print(a * c)  # Multiplication
elif b == "/":
    if c != 0:  # Checking if num3 is not zero to avoid division by zero error
        print(a / c)  # Division
    else:
        print("Division by zero is not allowed")  # Error message for division by zero
else:
    print("Error: Invalid operator")  # Error message for invalid operator input
