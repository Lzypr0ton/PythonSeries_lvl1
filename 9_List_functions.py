friends = ["Tony", "Chris", "Sachin", "May"]

# To find the index of a friend in the list:
print(friends.index('Chris'))  # This will print the index of 'Chris'

# To count occurrences of a particular name in the list:
print(friends.count("Chris"))

# To sort the list:
friends.sort()
print(friends)

# 1. append() function: Adds data to the current list
friends.append("Michael")
print(friends)

# 2. insert() function: Adds data at a specific position
friends.insert(2, "Sharukh")
print(friends)

# 3. pop() function: Removes the last element of the list (-1)
friends.pop()
print(friends)

# 4. remove() function: Removes data from the current list
friends.remove("Tony")
print(friends)

# 5. clear() function: Clears the entire list
friends.clear()
print(friends)
