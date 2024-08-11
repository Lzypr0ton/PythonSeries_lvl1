def max_num(num1, num2, num3):
    # Check if num1 is greater than or equal to num2 and num3
    if num1 >= num2 and num1 >= num3:
        return num1  # Return num1 if it is the largest
    elif num2 >= num1 and num2 >= num3:
        return num2  # Return num2 if it is the largest
    else:
        return num3  # Return num3 if it is the largest

# Test the function with sample inputs
a=input("enter num1:")
b=input("enter num2:")
c=input("enter num3:")
print(max_num(a,b,c))
