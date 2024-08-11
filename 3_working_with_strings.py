print("hello \n world")  # \n starts a new line
print("hello \t world")  # \t adds more space between the words
print("hello \\ world")  # The backslash character is escaped and printed

# Let's perform some string operations
phrase = "Rahul Jii"
print(phrase.lower())  # Prints the sentence in lowercase
print(phrase.upper())  # Prints the sentence in uppercase
print(phrase.islower())  # Gives a boolean value (True or False)
print(phrase.isupper())  # Gives a boolean value (True or False)

# We can chain these methods together as well
print(phrase.upper().isupper())  # This will print True

# The len() function counts the number of characters in a string, including spaces
print(len(phrase))

# Let's print specific characters using indexing
# Note: Indexing starts from 0
print(phrase[0])  # R
print(phrase[1])  # a
print(phrase[2])  # h
print(phrase[3])  # u
print(phrase[4])  # l
print(phrase[5])  # Space

# Now let's find the position of specific letters using index()
print(phrase.index("a"))  # Output is 1
print(phrase.index("Jii"))  # Output is 6 (where it starts to spell "Jii")

# Now let's see the replace() function
print(phrase.replace("Rahul", "Sachin"))  # Replaces "Rahul" with "Sachin"

# Just a reminder of other string functions as a revision:
"""
capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(),
find(), format(), format_map(), isalnum(), isalpha(), isdecimal(), isdigit(),
isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(),
isupper(), join(), ljust(), lower(), lstrip(), maketrans(), partition(), replace(),
rfind(), rindex(), rjust(), rpartition(), rsplit(), rstrip(), splitlines(),
startswith(), strip(), swapcase(), title(), translate(), upper(), zfill()
"""
