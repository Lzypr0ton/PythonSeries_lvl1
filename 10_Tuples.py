# NOTE: Tuples are IMMUTABLE
coordinates = (1, 2, 3, 4, 5)

# Accessing data from a tuple
print(coordinates[1])  # I can access data from a tuple but cannot perform operations like in a list

# Trying to modify an element in the tuple (which raises an error)
coordinates[1] = 69
# Results in a TypeError: 'tuple' object does not support item assignment
