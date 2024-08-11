# Dictionary mapping digits to their word representations
number_words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}

# Example usage of the dictionary with the .get() method
print(number_words.get(7))  # Output: Seven
print(number_words.get(11))  # Output: None (KeyError avoided)
