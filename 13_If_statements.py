is_student = input("Are you a student? ")
is_indian = input("Are you Indian? ")

# Using IF statement
if is_student.lower() == 'yes' or is_indian.lower() == 'yes':
    print("You are a student or Indian, or both.")

# Using IF-ELSE statement
if is_student.lower() == 'yes' or is_indian.lower() == 'yes':
    print("You are a student or Indian, or both.")
else:
    print("You are not a student or Indian, or both.")

# Using ELIF statement
if is_student.lower() == 'yes' and is_indian.lower() == 'yes':
    print("You are a student and Indian.")
elif is_indian.lower() == 'yes':
    print("You are Indian.")
elif is_student.lower() == 'yes':
    print("You are a student.")
else:
    print("You are neither a student nor Indian.")
