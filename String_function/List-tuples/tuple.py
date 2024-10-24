# Defining a tuple with mixed data types
my_tuple = ("hi", 1, 2, 3, 4, 5, "World")

# Print the type of the tuple
print("Type of my_tuple:", type(my_tuple))  # Output: <class 'tuple'>

# Print the tuple itself
print("Contents of my_tuple:", my_tuple)  # Output: ("hi", 1, 2, 3, 4, 5, "World")

# Print the length of the tuple
print("Length of my_tuple:", len(my_tuple))  # Output: 7

# Define a tuple with only numeric values
tuple1 = (1, 2, 3, 4, 5, 6, 47, 78)

# Print the tuple and its type
print("Contents of tuple1:", tuple1)         # Output: (1, 2, 3, 4, 5, 6, 47, 78)
print("Type of tuple1:", type(tuple1))       # Output: <class 'tuple'>

# Print the maximum and minimum values in the numeric tuple
print("Maximum value in tuple1:", max(tuple1))  # Output: 78
print("Minimum value in tuple1:", min(tuple1))  # Output: 1
