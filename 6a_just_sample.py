# Taking input from the user for two numbers
num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")

# Displaying the menu for operations
print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")

# Taking input for the desired operation
choice = input("Which operation do you want to perform: ")

# Converting user inputs (num1 and num2) from strings to floats for numerical operations
num1 = float(num1)
num2 = float(num2)

# Performing the selected operation based on user's choice
if choice == '1':  # Addition
    result = num1 + num2
elif choice == '2':  # Subtraction
    result = num1 - num2
elif choice == '3':  # Multiplication
    result = num1 * num2
elif choice == '4':  # Division
    if num2 != 0:  # Checking if num2 is not zero to avoid division by zero error
        result = num1 / num2
    else:
        result = "Division by zero is not allowed"
else:
    result = "Invalid choice"

# Printing the result of the operation
print("Result:", result)


